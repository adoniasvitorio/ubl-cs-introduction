#include<iostream>

int main() {
  int nota_1, nota_2, nota_3, nota_4;
  
  std::cout << "Digite a primeira nota ";
  std::cin >> nota_1;

  std::cout << "Digite a segunda nota";
  std::cin >> nota_2;

  std::cout << "Digite a terceira nota";
  std::cin >> nota_3;

  std::cout <<"Digite a quarta nota";
  std::cin >> nota_4;

  float media = (nota_1 + nota_2 + nota_3 + nota_4) / 4;
  std::cout << "A media aritmetica e " << media;
  
  return 0;
}
