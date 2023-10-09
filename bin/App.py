from AdjMatrix import AdjMatrix
import matplotlib.pyplot as plt
import networkx as nx
import random
import math

class App:
    def main():
        App.take_input_from_terminal()
        # App.take_input_from_file("../test/16x16/1.txt")

    def take_input_from_terminal():
        print("Input:")
        App.run(input())

    def take_input_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                App.run(file.read())
        except FileNotFoundError as e:
            print(e)

    def run(input_data):
        input_lines = input_data.strip().split('\n')
        num_terms, *terms = map(int, input_lines[0].split())

        result = App.max_hh(terms)
        # result = App.min_hh(terms)
        # result = App.ur_hh(terms)

        if result is not None:
            print(result)

            G = nx.Graph()

            num_nodes = result.size
            G.add_nodes_from(range(num_nodes))

            # Add edges to the graph based on the adjacency matrix
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):  # Only add edges for the upper triangular part (avoid duplicates)
                    if result.get(i, j) == 1:
                        G.add_edge(i, j)

            # Calculate positions for the nodes dynamically
            node_positions = {}
            for i in range(num_nodes):
                angle = (2 * math.pi * i) / num_nodes
                x = math.sin(angle)
                y = math.cos(angle)
                node_positions[i] = (x, y)

            # Draw the graph using Matplotlib with the calculated positions
            nx.draw(
                G,
                pos=node_positions,
                with_labels=True,
                node_color='skyblue',
                node_size=500,
                font_size=10,
                font_color='black',
                font_weight='bold'
            )

            # Add the graphic sequence as text above the graph
            sequence_str = 'Sequence: ' + ', '.join(map(str, terms))
            plt.annotate(
                sequence_str,
                xy=(0, 0),  # Position of the annotation (adjust as needed)
                xycoords='axes fraction',  # Coordinate system for the position
                fontsize=12,  # Font size for the annotation
                #ha='center'  # Horizontal alignment (centered)
            )

            plt.title("Graph Representation")
            plt.axis("off")  # Hide axis
            plt.show()

        else:
            print("The degree sequence", terms, "is not graphic")

    def max_hh(terms):
        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            k = len(bins) - 1
            while len(bins[k]) == 0:
                k -= 1

            pivot_node = sorted(bins[k]).pop(0)
            bins[k].remove(pivot_node)
            # print("Pivot node:", pivot_node)
            bins[0].add(pivot_node)
            # print(bins)
            cur_deg = k

            for i in range(k):
                while len(bins[cur_deg]) == 0 and cur_deg > 0:
                    cur_deg -= 1
                if cur_deg == 0:
                    return None
                else:
                    neighbor_node = sorted(bins[cur_deg]).pop(0)
                    bins[cur_deg].remove(neighbor_node)
                    moved_nodes[neighbor_node] = cur_deg - 1
                    result.add_edge(pivot_node, neighbor_node)
                    result.add_edge(neighbor_node, pivot_node)
                    # print("Added edge:", pivot_node, neighbor_node)
                    # print(bins)
            
            for k in moved_nodes.keys():
                bins[moved_nodes.get(k)].add(k)

            # print("Moved nodes")
            # print(bins)

            # for i in range(len(moved_nodes)):
            #     bins[moved_nodes_degs.pop()].add(moved_nodes.pop())

        return result
    
    def min_hh(terms):
        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            k = 1
            while len(bins[k]) == 0:
                k += 1

            pivot_node = sorted(bins[k]).pop(0)
            bins[k].remove(pivot_node)
            # print("Pivot node:", pivot_node)
            bins[0].add(pivot_node)
            # print(bins)
            cur_deg = len(terms) - 1

            for i in range(k):
                while len(bins[cur_deg]) == 0 and cur_deg > 0:
                    cur_deg -= 1
                if cur_deg == 0:
                    return None
                else:
                    neighbor_node = sorted(bins[cur_deg]).pop(0)
                    bins[cur_deg].remove(neighbor_node)
                    moved_nodes[neighbor_node] = cur_deg - 1
                    result.add_edge(pivot_node, neighbor_node)
                    result.add_edge(neighbor_node, pivot_node)
                    # print("Added edge:", pivot_node, neighbor_node)
                    # print(bins)
            
            for k in moved_nodes.keys():
                bins[moved_nodes.get(k)].add(k)

            # print("Moved nodes")
            # print(bins)

            # for i in range(len(moved_nodes)):
            #     bins[moved_nodes_degs.pop()].add(moved_nodes.pop())

        return result
    
    def ur_hh(terms):
        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]
        possible_pivots = list(range(len(terms)))

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            pivot_node = possible_pivots.pop(random.randint(0, len(possible_pivots) - 1))
            k = 0
            while pivot_node not in bins[k]:
                k += 1

            bins[k].remove(pivot_node)
            # print("Pivot node:", pivot_node)
            bins[0].add(pivot_node)
            # print(bins)
            cur_deg = len(terms) - 1

            for i in range(k):
                while len(bins[cur_deg]) == 0 and cur_deg > 0:
                    cur_deg -= 1
                if cur_deg == 0:
                    return None
                else:
                    neighbor_node = sorted(bins[cur_deg]).pop(0)
                    bins[cur_deg].remove(neighbor_node)
                    moved_nodes[neighbor_node] = cur_deg - 1
                    result.add_edge(pivot_node, neighbor_node)
                    result.add_edge(neighbor_node, pivot_node)
                    # print("Added edge:", pivot_node, neighbor_node)
                    # print(bins)
            
            for k in moved_nodes.keys():
                bins[moved_nodes.get(k)].add(k)

            # print("Moved nodes")
            # print(bins)

            # for i in range(len(moved_nodes)):
            #     bins[moved_nodes_degs.pop()].add(moved_nodes.pop())

        return result

if __name__ == "__main__":
    App.main()
