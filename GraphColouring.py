from collections import defaultdict

class Graph:
    def __init__ (self, subjects):
        self.subjects = subjects
        self.graph = defaultdict(list)
    
    def add_edge(self, subject1, subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def graph_coloring(self):
        color_map={}
        available_colors = set(range(1, len(self.subjects)+1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

            available_colors = available_colors - used_colors

            if available_colors:
                color_map[subject] = min(available_colors)
            else:
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map

    def get_minimum_time_slots(self):
        color_map = self.graph_coloring()
        return max(color_map.values())

if __name__ == "__main__":
    subjects = []
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        subjects.append(subject)

    graph = Graph(subjects)

    num_edges = int(input("Enter the number of subject relationships: "))
    for _ in range(num_edges):
        edge = input("Enter subject1 and subject2 separated by a space: ").split()
        subject1, subject2 = edge[0], edge[1]
        graph.add_edge(subject1, subject2)

    minimun_time_slots = graph.get_minimum_time_slots()
    print(f"Minimum time slots required: {minimun_time_slots}")
