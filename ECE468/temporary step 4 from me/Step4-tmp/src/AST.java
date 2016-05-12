import java.util.*;
public class AST {
    public static String rootequals; //since AST is only called from assignments, ':=' will always be the root. This will be called accordingly from the grammar file
    public static String leftChild; //for an AST since it is only initialized during an assignment statement, we will have have the left child as an identifier. We will be called accordingly from the grammar file
    public static ASTnode rightChild; //the right child could be either an identifier/literal, or another node which would essentially be a subtree. We will declare a different data structure ASTnode for this purpose
    public static Stack<ASTnode> nodestackframe = new Stack<ASTnode>(); //the right child will essentially be a node, consisting of successive left and right children of nodes. Thus, we need to keep pushing it onto the stack, so that we know which stage of the right subtree we are in
    //public static Iterator<ASTnode> iter = nodestackframe.iterator();
    public static String operatorSeen = "no"; //to distinguish between a := b and a := b + c

    public static void setAST(String root, String left) {
	rootequals = root;
	leftChild = left;
	rightChild = null;
    }

    public static void createTerminalNode(String text) {
	ASTnode node = new ASTnode(text, null, null); //create the terminal node. leftchild and rightchild will both be null
	nodestackframe.push(node);
	System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	//printStackCurr();
    }
    
    public static void createNonTerminalNode(String text) {
	ASTnode node = new ASTnode(text, nodestackframe.pop(), null); //create the non-terminal node. rightchild will both be null initially, but will be updated along the way. leftchild can be gotten by popping the current node in the stack
	nodestackframe.push(node); //push the newly created node into the stack
	operatorSeen = "yes";
	System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	
	//printStackCurr();
    }

    public static void popFinalNode() { //this function will essentially return the final node in the stack, which will contain the entire right child of the expression as a binary tree
	rightChild = nodestackframe.pop();//assign to the right child
	System.out.println("AT THE END. WILL PRINT THE FINAL CONTENTS OF STACK.");
	print();
    }
    
    public static void moveRightChildUp() { //this function will move up one level the right child
	if (operatorSeen == "no") { //only one terminal node was present then just return
	    //printStackCurr();
	    System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	    return;
	}
	else { //at least moving up needs to be done
	    ASTnode right = nodestackframe.pop(); //get the right node
	    ASTnode parent = nodestackframe.pop(); //get the parent. They are always going to be the topmost two
	    parent.rightChild = right; //make the assignment
	    System.out.println("After factor finishes, printing the subexpression...");
	    inorderTraversal(parent);
	    nodestackframe.push(parent); //now push the parent right back to the stack
	    System.out.println("Top element of the stack now: " + nodestackframe.peek().text);
	    //printStackCurr();
	    return;
	}
    }
    
    public static void print() { //print using inorder traversal
        inorderTraversal(rightChild); //print starting from the right child
    }

    public static void inorderTraversal(ASTnode curr) {
	if (curr == null) {
	    return;
	}
	inorderTraversal(curr.leftChild);
	System.out.println(curr.text + " ");
	inorderTraversal(curr.rightChild);
    }
	
    public static void printStackCurr() {
	
	ASTnode temp = nodestackframe.pop();
	inorderTraversal(temp);
	nodestackframe.push(temp);
	
	//while (iter.hasNext()) {
	    //ASTnode tmp = iter.next();
	    //System.out.println(tmp.text);
	//}
    }
	
}
