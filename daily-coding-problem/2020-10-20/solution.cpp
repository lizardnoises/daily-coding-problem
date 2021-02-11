#include <cstdint>

class Node {
public:
    int val;
    Node* both;
    Node(int val, Node* both);
};

Node::Node(int val, Node* both) {
    this->val = val;
    this->both = both;
}

class XorLinkedList {
public:
    XorLinkedList();
    ~XorLinkedList();
    void add(int element);
    Node* get(unsigned index);
private:
    Node* root;
    Node* XorPointers(Node* prev, Node* next);
};

XorLinkedList::XorLinkedList() {
    root = 0;
}

XorLinkedList::~XorLinkedList() {
    Node* prev = 0;
    Node* node = root;
    Node* next = 0;
    while (next = XorPointers(prev, node->both)) {
        prev = node;
        delete node;
        node = next;
    }
}

void XorLinkedList::add(int element) {
    Node* prev = 0;
    Node* node = root;
    Node* next = 0;
    while (next = XorPointers(prev, node->both)) {
        prev = node;
        node = next;
    }
    Node *newNode = new Node(element, XorPointers(node, 0));
    node->both = XorPointers(prev, newNode);
}

Node* XorLinkedList::get(unsigned index) {
    Node *prev = 0;
    Node *node = root;
    Node *next = 0;
    for (int i = 0; i < index; i++) {
        next = XorPointers(prev, node->both);
        prev = node;
        node = next;
    }
    return node;
}

Node* XorLinkedList::XorPointers(Node* prev, Node* next) {
    return reinterpret_cast<Node*>(
        reinterpret_cast<uintptr_t>(prev) ^
        reinterpret_cast<uintptr_t>(next)
    );
}