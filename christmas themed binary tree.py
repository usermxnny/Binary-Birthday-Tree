import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Node class for the tree
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Function to build a binary tree representing the Christmas tree
def build_christmas_tree(levels):
    """Build a binary tree with the specified number of levels."""
    root = TreeNode("*")  # Tree topper
    current_level = [root]

    for _ in range(1, levels):
        next_level = []
        for node in current_level:
            # Randomly assign decorations to left and right children
            node.left = TreeNode(random.choice(["@", "$", "*", "+"]))
            node.right = TreeNode(random.choice(["@", "$", "*", "+"]))
            next_level.extend([node.left, node.right])
        current_level = next_level

    return root

# Function to add colors to decorations
def decorate(value):
    """Add colors to decorations."""
    if value == "*":
        return Fore.YELLOW + value
    elif value == "@":
        return Fore.RED + value
    elif value == "$":
        return Fore.GREEN + value
    elif value == "+":
        return Fore.BLUE + value
    else:
        return value

# Function to visualize the Christmas tree
def visualize_tree(root, levels):
    """Display the binary tree in a Christmas tree shape."""
    if not root:
        return

    queue = [root]
    for level in range(levels):
        level_nodes = 2 ** level  # Number of nodes at this level
        padding = " " * (levels - level - 1)  # Space padding for centering
        line = padding

        for _ in range(level_nodes):
            if queue:
                current = queue.pop(0)
                line += f"{decorate(current.value)} "
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            else:
                line += " "
        print(line)

# Function to add a "presents" section below the tree
def add_presents(levels):
    """Add a row of presents under the tree."""
    presents = " ".join([Fore.MAGENTA + "P" for _ in range(2 ** levels)])
    print(" " * (levels - 1) + presents)

# Build and visualize the Christmas tree
levels = 3  # Number of levels in the tree
tree_root = build_christmas_tree(levels)
print(Style.BRIGHT + "\n🎄 Christmas Tree 🎄\n")
visualize_tree(tree_root, levels)
add_presents(levels)
