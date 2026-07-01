import streamlit as st
import networkx as nx
import plotly.graph_objects as go


def relationship_graph(events):

    st.subheader("🔗 Relationship Graph")

    graph = nx.Graph()

    for event in events:

        if event.username:
            graph.add_node(event.username)

        if event.hostname:
            graph.add_node(event.hostname)

        if event.process:
            graph.add_node(event.process)

        if event.source_ip:
            graph.add_node(event.source_ip)

        if event.username and event.hostname:
            graph.add_edge(event.username, event.hostname)

        if event.username and event.process:
            graph.add_edge(event.username, event.process)

        if event.hostname and event.process:
            graph.add_edge(event.hostname, event.process)

        if event.hostname and event.source_ip:
            graph.add_edge(event.hostname, event.source_ip)

    if graph.number_of_nodes() == 0:
        st.info("No relationships found.")
        return

    pos = nx.spring_layout(graph, seed=42)

    edge_x = []
    edge_y = []

    for edge in graph.edges():

        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        hoverinfo="none"
    )

    node_x = []
    node_y = []
    node_text = []

    for node in graph.nodes():

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)
        node_text.append(str(node))

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        hovertext=node_text,
        hoverinfo="text",
        marker=dict(
            size=16,
            line_width=2
        )
    )

    fig = go.Figure(
        data=[edge_trace, node_trace]
    )

    fig.update_layout(
        height=650,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )