import streamlit as st

from modules.config import *
from modules.inventory import *
from modules.rag import *
from modules.ui import *

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Aegis",
    page_icon="🛡️",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

inventory_df = load_inventory(
    INVENTORY_FILE
)

db = load_vectordb()

llm = load_llm()

# =====================================================
# METRICS
# =====================================================

total_instances = len(
    inventory_df
)

prod_instances = len(
    inventory_df[
        inventory_df["environment"] == "PROD"
    ]
)

tier1_instances = len(
    inventory_df[
        inventory_df["tier"] == "Tier-1"
    ]
)

regions = inventory_df["region"].nunique()

# =====================================================
# UI
# =====================================================

render_header()

render_metrics(
    total_instances,
    prod_instances,
    tier1_instances,
    regions
)

render_sidebar()

# =====================================================
# SEARCH
# =====================================================

question = st.text_area(
    "Ask Aegis",
    height=120,
    placeholder="""
Examples:

inventory: environment=PROD

inventory: environment=PROD,tier=Tier-1

inventory: count by environment

How do I check replication status?

How do I investigate write latency?
"""
)

if st.button(
    "Analyze",
    use_container_width=True
):

    question_lower = (
        question.lower().strip()
    )

    # =============================================
    # INVENTORY
    # =============================================

    if question_lower.startswith(
        "inventory:"
    ):

        inventory_query = (
            question[10:]
            .strip()
        )

        result = process_inventory_query(
            inventory_query,
            inventory_df
        )

        st.markdown(
            "## Aegis Recommendation"
        )

        if isinstance(result, str):

            st.warning(result)

        else:

            st.success(
                f"{len(result)} records found"
            )

            st.dataframe(
                result,
                use_container_width=True
            )

        st.divider()

        st.markdown(
            "### Evidence Used"
        )

        st.info(
            INVENTORY_FILE
        )

    # =============================================
    # OPERATIONS
    # =============================================

    else:

        with st.spinner(
            "Analyzing operational guidance..."
        ):

            answer, results = (
                search_runbooks(
                    question,
                    db,
                    llm
                )
            )

        st.markdown(
            "## Aegis Recommendation"
        )

        st.info(answer)

        with st.expander(
            "Evidence Used"
        ):

            for doc, score in results:

                st.markdown(
                    f"### {doc.metadata.get('filename','Unknown')}"
                )

                st.write(
                    f"Category: {doc.metadata.get('folder','Unknown')}"
                )

                st.write(
                    f"Relevance Score: {round(score,4)}"
                )

                st.code(
                    doc.page_content[:1000]
                )

# =====================================================
# FOOTER
# =====================================================

render_footer()