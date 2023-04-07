#include <iostream>
#include <cmath>
using namespace std;
int main() 
{
    double a = 0.0;
    double b = 2.0;
    double c = 0;
    double saiSo = 0.01;
    int n = 0;
    
    while(1)
    {
        n++;
        c = (a-b)/2;
        if ((a*a-3*a -5) * (c*c - 3 * c - 5) < 0)
            b = c;
        else
            a = c;
            
        saiSo = abs(b-a);
        if (saiSo < 0.01)
            break;
    }
    cout << "Nghiem cua phuong trinh la: " << c << endl;
    cout << "So lan lap: " << n << endl;
    return 0;
}