

//list的链式实现
class Node {
public:
	int data;
	Node *next;

};

class listlk{
public:
	Node *head;
	


	listlk() {
		head = new Node;
		head->data = 0;
		head->next = 0;

	}
	bool isempty() {
		return head->next == 0;
	}
	bool Delete(int k) {				
		if (isempty())return false;
		else {
			Node *ptr = head;
			for (int i = 0; i < k; i++)
			{
				ptr = ptr->next;
			}
			Node *temp = ptr->next;
			ptr->next = ptr->next->next;
			delete temp;
			return true;
		}
	}
	int insert(int k, int e) {
		if (k == 0)return false;
		else {
			Node temp;
			temp.data = e;
			Node *ptr = head;
			for (int i = 0; i < k; i++)
			{
				ptr = ptr->next;
			}
			ptr->next = temp.next;
			temp.next = ptr;
			return true;
		}
	}
	int length() {
		int i = 0;
		Node *ptr = head;
		while (ptr != 0) {
			i++;
		}
		return i;
	}

	int find(int k) {
		Node *ptr = head;
		for (int i = 0; i < k; i++)
		{
			ptr = ptr->next;
		}
		int e = ptr->data;
		return e;
	}

	~listlk() {
		int i = 0;
		while (!isempty())
		{
			Delete(i);
			i++;
		}
	}

};
