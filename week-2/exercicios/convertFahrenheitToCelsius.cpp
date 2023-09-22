#include<iostream>

int main() {
  float fahrenheit, valueInCelsius;
  
  std::cout << "Digite uma temperatura em Fahrenheit: ";
  std::cin >> fahrenheit;

  valueInCelsius = (fahrenheit - 32) * 5/9;
  std::cout << "A temperatura em Celsius e: " << valueInCelsius <<std::endl;

  return 0;
}
