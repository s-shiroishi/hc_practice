import random 

class Grouping:
    def __init__(self, members: list[str]):
        if not isinstance(members, list):
            raise ValueError('グループはリスト形式で指定してください。')
        if len(members) != 6:
            raise ValueError('グループは6人でなければなりません。')
        self.members = members
    
    
    def divide_group(self) -> tuple[list[str], list[str]]:
        size = random.choice([2, 3])
        group_a = random.sample(self.members, size)
        group_b = [member for member in self.members if member not in group_a]

        if len(group_a) + len(group_b) != 6:
            raise ValueError('グループ分けに失敗しました。')
        
        return   group_a, group_b

def initialize_and_print_groups(members: list[str]):
    groups = Grouping(members).divide_group()
    for group in groups:
        sorted_group = sorted(group)
        print(sorted_group)

if __name__ == '__main__':
    initialize_and_print_groups(['A', 'B', 'C', 'D', 'E', 'F'])