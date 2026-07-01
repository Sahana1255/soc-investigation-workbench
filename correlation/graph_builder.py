class GraphBuilder:

    def build(self, relationships):

        nodes = set()

        edges = []

        for relation in relationships:

            nodes.add(relation.source)
            nodes.add(relation.target)

            edges.append(
                (
                    relation.source,
                    relation.target,
                    relation.relationship_type
                )
            )

        return {

            "nodes": list(nodes),

            "edges": edges

        }