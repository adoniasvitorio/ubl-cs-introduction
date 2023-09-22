#include<iostream>

int main() {
  int input;
  std::cout << "Digite o valor correspondente ao lado de um quadrado";
  std::cin >> input;

  int perimetro = 4 * input;
  int area = input * input;

  std::cout << "perimetro " << perimetro;
  std::cout << " - area " << area <<std::endl;
  
  return 0;
}
