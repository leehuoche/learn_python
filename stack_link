
//栈的链式实现

class Node {
public:
	int data;
	Node *next;
};
class stacklk
{
public:
	Node *top;
	stacklk() {
		top = new Node;
		top->data = -88;
		top->next = 0;
		
	}
	
	bool push(int e) {
		
		Node *temp;
		if (temp = new Node) {
			temp->data = e;
			temp->next = top->next;
			top = temp;
			return true;
		}
		else {
			return false;
		}
		
	}

	bool isempty() { return top->next == 0; }
	bool pop() {
		if (!isempty())
		{
			Node *tem;
			tem = top;
			top = top->next;
			delete tem;

		}
		else { return false; }
	}

	bool popE(int e) {
		e = top->data;
		pop();
		return e;

	}


	bool clear() {
		if (top->next == 0)
		{
			return false;

		}
		else {
			while (top->next == 0)
			{
				pop();
			}
			return  true;
		}
	}

	int length() {
		if (isempty())
			return 0;
		else {
			Node *ptr;
			ptr = top;
			int i = 0;
			while (ptr->next != 0)
				i++;
			return i;
		}
		
	}

	~stacklk() {
		clear();
		delete top;
	}



};

