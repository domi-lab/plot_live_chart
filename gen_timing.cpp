// Author: domi-lab
// Function:
// - Generate random data in C++.

#include <iostream>
#include <fstream>
#include <unistd.h>

using namespace std;

int main()
{
  fstream fout;
  int frame_counter = 0;
  float module_1 = 0, module_2 = 0, module_3 = 0, module_4 = 0, module_5 = 0;
  remove("../timing.csv");                         //remove file named timing.csv in folder
  fout.open("../timing.csv", ios::out | ios::app); // opens an existing csv file or creates a new file.

  // Write name of each module in csv file
  fout << "frame"
       << ","
       << "module_1"
       << ","
       << "module_2"
       << ","
       << "module_3"
       << ","
       << "module_4"
       << ","
       << "module_5"
       << "\n";

  while (1)
  {
    // opens an existing csv file or creates a new file.
    fout.open("../timing.csv", ios::out | ios::app); // opens an existing csv file or creates a new file.
    frame_counter++;
    module_1 = (rand() % 6) + 5;
    module_2 = (rand() % 10) + 15;
    module_3 = (rand() % 20) + 25;
    module_4 = (rand() % 5) + 3;
    module_5 = (rand() % 50) + 45;
    // Insert the data to file
    fout << frame_counter << ", " << module_1 << ", " << module_2 << ", " << module_3 << ", " << module_4 << ", " << module_5 << "\n";
    fout.close();
    cout << frame_counter << ", " << module_1 << ", " << module_2 << ", " << module_3 << ", " << module_4 << ", " << module_5 << "\n";
    usleep(60000);
    cout << "generate random values every 60ms" << endl;
  }
  return 0;
}
