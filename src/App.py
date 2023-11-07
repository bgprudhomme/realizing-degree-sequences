from AdjMatrix import AdjMatrix
import matplotlib.pyplot as plt
import networkx as nx
import random
import math

class App:
    def main():
        # App.take_input_from_terminal()
        # App.take_input_from_file()
        App.reg2_rand_test(6, -2)
        App.reg2_rand_test(6, -1)
        App.reg2_rand_test(6, 0)
        App.reg2_rand_test(6, 1)
        App.reg2_rand_test(6, 2)
        App.reg2_rand_test(7, -2)
        App.reg2_rand_test(7, -1)
        App.reg2_rand_test(7, 0)
        App.reg2_rand_test(7, 1)
        App.reg2_rand_test(7, 2)
        App.reg2_rand_test(8, -2)
        App.reg2_rand_test(8, -1)
        App.reg2_rand_test(8, 0)
        App.reg2_rand_test(8, 1)
        App.reg2_rand_test(8, 2)
        App.reg2_rand_test(9, -2)
        App.reg2_rand_test(9, -1)
        App.reg2_rand_test(9, 0)
        App.reg2_rand_test(9, 1)
        App.reg2_rand_test(9, 2)

    def take_input_from_terminal():
        while True:
            print("Input:")
            App.run(input())

    def take_input_from_file():
        print("File path:")
        file_path = input()
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    App.run(line)
        except FileNotFoundError as e:
            print(e)

    def reg2_rand_test(n, x):
        random.seed(0)
        seq = [2] * n
        print("n =", n, "x =", x)
        sims = 10000
        graph1 = 0
        graph2 = 0
        graph3 = 0
        graph4 = 0
        
        for i in range(sims):
            # print("Sim", i+1, "/", sims)
            result = App.parr_hh(seq, x).cycleLens()
            if n == 6:
                if result[0] == 3 and result[1] == 3:
                    graph1 += 1
                if result[0] == 6:
                    graph2 += 1
            if n == 7:
                if result[0] == 3 and result[1] == 4:
                    graph1 += 1
                if result[0] == 7:
                    graph2 += 1
            if n == 8:
                if result[0] == 3 and result[1] == 5:
                    graph1 += 1
                if result[0] == 4 and result[1] == 4:
                    graph2 += 1
                if result[0] == 8:
                    graph3 += 1
            if n == 9:
                if result[0] == 3 and result[1] == 3 and result[2] == 3:
                    graph1 += 1
                if result[0] == 3 and result[1] == 6:
                    graph2 += 1
                if result[0] == 4 and result[1] == 5:
                    graph3 += 1
                if result[0] == 9:
                    graph4 += 1
        
        if n == 6:
            print("(3, 3):", graph1 / sims)
            print("(6):", graph2 / sims)
        if n == 7:
            print("(3, 4):", graph1 / sims)
            print("(7):", graph2 / sims)
        if n == 8:
            print("(3, 5):", graph1 / sims)
            print("(4, 4):", graph2 / sims)
            print("(8):", graph3 / sims)
        if n == 9:
            print("(3, 3, 3):", graph1 / sims)
            print("(3, 6):", graph2 / sims)
            print("(4, 5):", graph3 / sims)
            print("(9):", graph4 / sims)

    def run(input_data):
        input_lines = input_data.strip().split('\n')
        num_terms, *terms = map(int, input_lines[0].split())

        while len(terms) < num_terms:
            new_terms = map(int, input().split())
            terms.extend(new_terms)
 
        result = App.max_hh(terms)

        # result = App.parr_hh(terms, 1)
        # result = App.pr_hh(terms)

        # result = App.parr_hh(terms, 0)
        # result = App.ur_hh(terms)
        
        # result = App.parr_hh(terms, -1)
        
        # result = App.min_hh(terms)

        if result is not None:
            # print(result)

            G = nx.Graph()

            num_nodes = result.size
            node_labels = {i: chr(65 + i) for i in range(num_nodes)}

            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    if result.get(i, j) == 1:
                        G.add_edge(node_labels[i], node_labels[j])

            node_positions = {}
            for i, label in node_labels.items():
                angle = (2 * math.pi * i) / num_nodes
                x = math.sin(angle)
                y = math.cos(angle)
                node_positions[label] = (x, y)

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

            sequence_str = 'Sequence: ' + ', '.join(map(str, terms))
            plt.annotate(
                sequence_str,
                xy=(0, 0),
                xycoords='axes fraction',
                fontsize=12,
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
        transfers = 0

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
            transfers += 1
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
                transfers += 1

            # print("Moved nodes")
            # print(bins)

        print(transfers, "transfers")

        return result
    
    def min_hh(terms):

        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            if term >= len(terms):
                return None
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0
        transfers = 0

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
            transfers += 1
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
                transfers += 1

            # print("Moved nodes")
            # print(bins)

        print(transfers, "transfers")

        return result
    
    def ur_hh(terms):

        # random.seed(0)

        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0
        transfers = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            num_nonzero_degs = sum((0 if i == 0 else 1) * len(bins[i]) for i in range(len(terms)))
            bin_probabilities = [(0 if i == 0 else 1) * len(bins[i]) / num_nonzero_degs for i in range(len(terms))]
            # print("Bin probabilities:", bin_probabilities)  
            
            pivot_bin = random.choices(range(len(terms)), bin_probabilities)[0]
            # print("Pivot bin:", pivot_bin)  
                          
            pivot_node = random.choice(list(bins[pivot_bin]))
            # print("Pivot node:", pivot_node)  

            bins[pivot_bin].remove(pivot_node)
            bins[0].add(pivot_node)
            transfers += 1
            # print(bins)
            cur_deg = len(terms) - 1

            for i in range(pivot_bin):
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
                transfers += 1

        print(transfers, "transfers")

            # print("Moved nodes")
            # print(bins)

            # for i in range(len(moved_nodes)):
            #     bins[moved_nodes_degs.pop()].add(moved_nodes.pop())

        return result
    
    def pr_hh(terms):
        # random.seed(0)

        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0
        transfers = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            deg_sum = sum(i * len(bins[i]) for i in range(len(terms)))
            bin_probabilities = [i * len(bins[i]) / deg_sum for i in range(len(terms))]
            # print("Bin probabilities:", bin_probabilities)  
            
            pivot_bin = random.choices(range(len(terms)), bin_probabilities)[0]
            # print("Pivot bin:", pivot_bin)  
                          
            pivot_node = random.choice(list(bins[pivot_bin]))
            # print("Pivot node:", pivot_node)  

            bins[pivot_bin].remove(pivot_node)
            bins[0].add(pivot_node)
            transfers += 1
            # print(bins)
            cur_deg = len(terms) - 1

            for i in range(pivot_bin):
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
                transfers += 1

        print(transfers, "transfers")

            # print("Moved nodes")
            # print(bins)

        return result
    
    def parr_hh(terms, x):
        # random.seed(0)

        result = AdjMatrix(len(terms))

        bins = [set() for _ in range(len(terms))]

        for i, term in enumerate(terms):
            bins[term].add(i)
        
        # print(bins)
        
        rounds = 0
        transfers = 0

        while len(bins[0]) != len(terms):
            moved_nodes = {}
            rounds = rounds + 1
            # print("Round", rounds)

            deg_sum = sum((0 if i == 0 else pow(i, x)) * len(bins[i]) for i in range(len(terms)))
            bin_probabilities = [(0 if i == 0 else pow(i, x)) * len(bins[i]) / deg_sum for i in range(len(terms))]
            # print("Bin probabilities:", bin_probabilities)  
            
            pivot_bin = random.choices(range(len(terms)), bin_probabilities)[0]
            # print("Pivot bin:", pivot_bin)  
                          
            pivot_node = random.choice(list(bins[pivot_bin]))
            # print("Pivot node:", pivot_node)  

            bins[pivot_bin].remove(pivot_node)
            bins[0].add(pivot_node)
            transfers += 1
            # print(bins)
            cur_deg = len(terms) - 1

            for i in range(pivot_bin):
                while len(bins[cur_deg]) == 0 and cur_deg > 0:
                    cur_deg -= 1
                if cur_deg == 0:
                    return None
                else:
                    neighbor_node = sorted(list(bins[cur_deg])).pop(0)
                    bins[cur_deg].remove(neighbor_node)
                    moved_nodes[neighbor_node] = cur_deg - 1
                    result.add_edge(pivot_node, neighbor_node)
                    result.add_edge(neighbor_node, pivot_node)
                    # print("Added edge:", pivot_node, neighbor_node)
                    # print(bins)
            
            for k in moved_nodes.keys():
                bins[moved_nodes.get(k)].add(k)
                transfers += 1

            # print("Moved nodes")
            # print(bins)

        # print(transfers, "transfers")

        # print(result)

        return result

if __name__ == "__main__":
    App.main()
