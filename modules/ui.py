import streamlit as st


def render_header():

    st.title("🛡️ Aegis")

    st.markdown("""
### Aurora PostgreSQL Operations Copilot

Accelerate troubleshooting, operational execution,
inventory visibility and platform awareness
across Aurora PostgreSQL environments.
""")

    st.divider()


def render_metrics(
    total_instances,
    prod_instances,
    tier1_instances,
    regions
):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Aurora Instances",
        f"{total_instances:,}"
    )

    c2.metric(
        "Production Instances",
        f"{prod_instances:,}"
    )

    c3.metric(
        "Tier-1 Instances",
        f"{tier1_instances:,}"
    )

    c4.metric(
        "Regions Covered",
        regions
    )

    st.divider()


def render_sidebar():

    with st.sidebar:

        st.header("Operational Readiness")

        st.success("Platform Coverage Active")

        st.divider()

        st.header("Capabilities")

        st.markdown("""
✅ Inventory Discovery

✅ Operational Guidance

✅ Runbook Search

✅ Troubleshooting Assistance

✅ Platform Visibility

✅ Upgrade Readiness
""")

        st.divider()

        st.header("Suggested Questions")

        st.code("""
inventory: environment=PROD

inventory: environment=PROD,tier=Tier-1

inventory: region=us-east-1

inventory: engine_version=16.4

inventory: criticality=Critical

inventory: count by environment

inventory: count by region

inventory: count by tier

How do I check replication status?

How do I investigate write latency?
""")


def render_footer():

    st.divider()

    st.caption(
        "Aegis | Aurora PostgreSQL Operations Copilot"
    )