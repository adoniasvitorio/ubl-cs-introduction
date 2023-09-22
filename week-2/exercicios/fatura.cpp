#include<iostream>

int main() {
  char nome[10], mes[10];
  int dia;
  float valor;

  std::cout << "Digite o nome do cliente: ";
  std::cin >> nome;

  std::cout << "Digite o dia de vencimento: ";
  std::cin >> dia;

  std::cout << "Digit o mes de vencimento: ";
  std::cin >> mes;

  std::cout << "Digite o valor da fatura: ";
  std::cin >> valor;

  std::cout << "Ola, " << nome <<"\n";
  std::cout << "A sua fatura com vencimento em " << dia;
  std::cout << " de " << mes;
  std::cout << " no valor de R$ " << valor;
  std::cout << " esta fechada." << std::endl; 
  
  return 0;
}
