from collections import defaultdict

# Build a dictionary of links between nodes
def build_links(data):
    links = defaultdict(set)
    for a, b in [data.split("-") for data in data.strip().split("\n")]:
        links[a].add(b)
        links[b].add(a)
    
    return links

# Find all groups of 3 where a node starts with 't'
def find_t3_groups(links):
    groups = set(tuple(sorted([n1, n2, n3])) for n1 in links 
                                             for n2 in links[n1] 
                                             for n3 in links[n1] 
                                             if n1.startswith("t") 
                                             and n3 in links[n2])
    return groups

# Find all complete networks of nodes
def find_complete_networks(links):
    networks = set()

    for n1 in links:
        for n2 in links[n1]:
            network = set.intersection(*({n} | links[n] for n in links[n1] if n != n2))
            networks.add(tuple(sorted(network)))
    
    return networks

# Test data
data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

# Read input
with open("input.txt", "r") as file:
    data = file.read()

# Parse data
links = build_links(data)

# Part 1
groups = find_t3_groups(links)
print(f"Part 1: {len(groups)}")

# Part 2
networks = find_complete_networks(links)
largest_network = max(networks, key=len)
print(f"Part 2: {",".join(sorted(largest_network))}")
