#include <iostream>

using namespace std;

int main()
{
	int a, b;
	cin >> a;
	cin >> b;
	if (a < b)
		cout << a;
		cout << "<" << b << endl;
	else
	{
		cout << a;
		cout << ">=" << b << endl;
	}

	for (int i = 0; i < 10; ++i)
		cout << "Hello World!" << endl;
	return 0;
}