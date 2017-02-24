
//栈的顺序实现
class stackse {
public:
	int *base, *top;
	int size;//栈的现在的最大容量
	int length;
	//构造函数
	stackse(int inisize = 30) {
		base = new int[inisize];
		top = base;
		size = inisize;
		length = 0;
	}
	//入栈
	bool push(int e) {
		if (length < size) {
			top = &e;
			top++;
			length++;
			return true;
		}
		else
		{
			return false;
		}
	}
	//出栈不返回值；
	bool pop() {
		if (top == base)
			return false;
		else
		{
			top--;
			return true;
		}
	}
	//出栈返回值
	int popE(int e) {
		e = *top;
		pop();
		return e;

	}
	//栈的长度
	int length(){
		return length;
	}
	//析构
	~stackse()
	{
		clear();
		delete base;
			
	}
	//置空
	bool clear(){
		if (top==base)
		{
			return false;

		}
		else {
			while (top != base)
			{
				pop();
			}
			return  true;
		}
	}
	//空否
	bool isempty() {
		return top == base;
	}
	//栈顶
	int gettop() {
		if (!isempty())
		{
			int e = *(top - 1);
			return e;
		}
		else
			return -100;
	}

};
