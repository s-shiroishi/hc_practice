import random 

class Group:
    def __init__(self, members: list[str]):
        if not isinstance(members, list):
            raise ValueError('グループはリスト形式で指定してください。')
        if len(members) != 6:
            raise ValueError('グループは6人でなければなりません。')
        self.members = members

class Grouping:
    def __init__(self, group: Group):
        self.group = group
        self.grouped_groups = []
    
    def _select_grouping_members(self):
        size = 3 if random.random() > 0.5 else 2
        return random.sample(range(len(self.group.members)), size)
    
    def grouping(self):
        selected_members = self._select_grouping_members() 
        new_group = [self.group.members[person] for person in selected_members]
        self.grouped_groups.append(new_group)
        self.grouped_groups.append(list(set(self.group.members) - set(new_group)))
        return self.grouped_groups

def initialize_and_print_groups(members: list[str]):
    groups = Grouping(Group(members)).grouping()
    for group in groups:
        sorted_group = sorted(group)
        print(sorted_group)

if __name__ == '__main__':
    initialize_and_print_groups(['A', 'B', 'C', 'D', 'E', 'F'])