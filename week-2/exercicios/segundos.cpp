#include<iostream>

int main() {
  int input;

  std::cout << "Digite o numero de segundos que deseja converter: ";
  std::cin >> input;

  int secondsInMinutes = 60;
  int secondsInHours =  secondsInMinutes * 60;
  int secondsInDays = secondsInHours * 24;

  int days = input / secondsInDays;
  input %= secondsInDays;

  int hours = input / secondsInHours;
  input %= secondsInHours;

  int minutes = input / secondsInMinutes;
  int seconds = input % secondsInMinutes; 
  
  std::cout << days <<    " dias,";
  std::cout << hours <<   " horas,";
  std::cout << minutes << " minutos e ";
  std::cout << seconds << " segundos"<< std::endl;
  
  return 0;
}
