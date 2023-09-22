#include<iostream>

int main() {
  int input;
  std::cout << "Digite um numero inteiro: ";
  std::cin >> input;

  int dezenas = (input / 10) % 10;
  std::cout << "O digito das dezendas e " << dezenas <<std::endl;
  return 0;
}
