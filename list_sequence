//list的顺序实现
class list_se
{
public:
	list_se() {
		length = 0;
		ele = new int[inisize];
	}
	bool isempty() {
		return length == 0;
	}
	//寻找第K个数
	int find(int k) {
		int x;
		x = ele[k];
		return x;

	}
	bool Delete(int k) {
		if (length == 0)return false;
		else {
			for (int i = k; i < length; i++)

				ele[i - 1] = ele[i];
			length--;
			return true;
		}
		
	}
	int Delete_num(int k) {
		int x = ele[k];
		Delete(k);
		return x;
	}
	bool insert(int k, int e) {
		if (length >= inisize)return false;
		else {
			for (int i = length; i >=k; i--)
			{
				ele[i + 1] = ele[i];
				ele[k] = e;

			}
			length++;
			return true;
		}
	}


	~list_se() {
		delete[]ele;
	}

private:

	int length;
	int inisize = 30;
	int *ele;
};


