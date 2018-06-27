import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

private static class NodeDepthPair {

    BinaryTreeNode node;
    int depth;

    NodeDepthPair(BinaryTreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}

public static boolean isBalanced(BinaryTreeNode treeRoot) {

    if (treeRoot == null) {
        return true;
    }

    List<Integer> depths = new ArrayList<>(3);

 
    Stack<NodeDepthPair> nodes = new Stack<>();
    nodes.push(new NodeDepthPair(treeRoot, 0));

    while (!nodes.empty()) {

     
        NodeDepthPair nodeDepthPair = nodes.pop();
        BinaryTreeNode node = nodeDepthPair.node;
        int depth = nodeDepthPair.depth;

     
        if (node.left == null && node.right == null) {

          
            if (!depths.contains(depth)) {
                depths.add(depth);

                if (depths.size() > 2 || (depths.size() == 2
                        && Math.abs(depths.get(0) - depths.get(1)) > 1)) {
                    return false;
                }
            }

 
        } else {
            if (node.left != null) {
                nodes.push(new NodeDepthPair(node.left, depth + 1));
            }
            if (node.right != null) {
                nodes.push(new NodeDepthPair(node.right, depth + 1));
            }
        }
    }

    return true;
}
