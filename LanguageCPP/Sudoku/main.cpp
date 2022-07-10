//Sudoku game (console and creating svg file of the game
#include<iostream>
#include<iomanip>
#include<ctime>
#include<string>
#include<locale>
#include<Windows.h>
#include <fstream>
#include<conio.h>
#include <vector>
#include <sstream>

using namespace std;

enum eDerection { STOP = 0, LEFT, RIGHT, UP, DOWN };
//Colors
enum ConsoleColor{
	Black = 0,
	Blue = 1,
	Green = 2,
	Aqua = 3,
	Red = 4,
	Purple = 5,
	Brown = 6,
	LightGray = 7,
	DarkGray = 8,
	LightBlue = 9,
	LightGreen = 10,
	LightAqua = 11,
	LightRed = 12,
	LightPurple = 13,
	Yellow = 14,
	White = 15
};
//Color change
int Color(ConsoleColor text, ConsoleColor background){
	HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hStdOut, (WORD)((background << 4) | text)); //текст | фон (цвет только с текстом)
	return 0;
}


class Board {
private:
    string table[3][3][3][3];
    string task[3][3][3][3];
    string gameTable[3][3][3][3];
    string filename = "sudokuTables.txt";
    string tables[6][81];

public:
    Board(){
        downloadTable();
        createTable();
        createTask();
        createGameTable();
        //displayBoard();
    }
    void downloadTable(){
        ifstream sudokuTables(filename);
        string sTables;
        int i=0;
        while (getline(sudokuTables, sTables)){
            for (int j = 0; j < sTables.length(); j = j+2){
                tables[i][j/2] = sTables[j];
            }
            i++;
        }
        cout << "File readed" << endl;
    }
    void createTable(){
        int taskN = randomNum(sizeof(tables) / sizeof(string) / 81);
        cout << "Table creation (" << taskN << ")" << endl;
        int numId = 0;
        for (int r = 0; r < 3; r++){
            for (int c = 0; c < 3; c++){
                for (int i = 0; i < 3; i++){
                    for (int j = 0; j < 3; j++){
                        table[r][c][i][j] = tables[taskN][numId];
                        numId++;
                    }
                }
            }
        }

    }
    void createTask(){
        for (int r = 0; r < 3; r++){
            for (int c = 0; c < 3; c++){
                for (int i = 0; i < 3; i++){
                    for (int j = 0; j < 3; j++){
                        if (randomNum(10) <= 3){

                            task[r][c][i][j] = "0";
                        }
                        else{
                            task[r][c][i][j] = table[r][c][i][j];
                        }
                    }
                }
            }
        }
    }
    void createGameTable(){
        for (int r = 0; r < 3; r++){
            for (int c = 0; c < 3; c++){
                for (int i = 0; i < 3; i++){
                    for (int j = 0; j < 3; j++){
                        gameTable[r][c][i][j] = task[r][c][i][j];
                    }
                }
            }
        }
    }
    int randomNum(int n){
        //srand(time(0));
        int num = rand() % n;
        return num;
    }
    void displayBoard(int ry=0, int cx=0, int iy=0, int jx=0, string BGcolor = "white"){
        system("cls");
        if (BGcolor == "white"){
            Color(White, Black);
        }
        cout << endl << "------------------------------" << endl;

        for (int r = 0; r < 3; r++){
            for (int i = 0; i < 3; i++){
                for (int c = 0; c < 3; c++){
                    for (int j = 0; j < 3; j++){
                        if (r == ry && c == cx && i == iy && j == jx){ Color(Black, Yellow); }
                        cout << " " << gameTable[r][c][i][j] << " ";
                        if (BGcolor == "white"){
                            Color(White, Black);
                        }
                    }
                    cout << "|";
                }
                cout << endl;
            }
            cout << "------------------------------" << endl;
        }
        Color(White, Black);
    }
    void placeNumber(string num, int ry=0, int cx=0, int iy=0, int jx=0){
        if (task[ry][cx][iy][jx] == "0"){
            gameTable[ry][cx][iy][jx] = num;
        }
    }
    bool check(){
        bool solve = true;
        for (int r = 0; r < 3; r++){
            for (int c = 0; c < 3; c++){
                for (int i = 0; i < 3; i++){
                    for (int j = 0; j < 3; j++){
                        if (gameTable[r][c][i][j] != table[r][c][i][j]){
                            solve = false;
                        }
                    }
                }
            }
        }
        return solve;
    }
    void printSVG(){
        string fileName = "svgHead.txt";
        ifstream file1(fileName.c_str());
        stringstream svgHead;
        svgHead << file1.rdbuf();

        ofstream outFile("images/board.svg");
        outFile << svgHead.rdbuf();
        string grid[9][9];

        int ii = 0;
        int jj = 0;
        for (int r = 0; r < 3; r++){
            for (int i = 0; i < 3; i++){
                for (int c = 0; c < 3; c++){
                    for (int j = 0; j < 3; j++){
                        grid[ii][jj] = task[r][c][i][j];
                        jj++;
                    }
                }
                jj = 0;
                ii++;
            }
        }

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(grid[i][j]!="0"){
                    int x = 50*j + 16;
                    int y = 50*i + 35;

                    stringstream text;
                    text<<"<text x=\""<<x<<"\" y=\""<<y<<"\" style=\"font-weight:bold\" font-size=\"30px\">"<<grid[i][j]<<"</text>\n";

                    outFile << text.rdbuf();
                }
            }
        }
        outFile << "</svg>";

    }
    string createImgNumber(int n){
        string num;
        if (n % 10 < 10){
            string num = "0000"+n;
        }
        else if (n % 100 < 100){
            string num = "000"+n;
        }
        else if (n % 1000 < 1000){
            string num = "00"+n;
        }
        else if (n % 10000 < 10000){
            string num = "0"+n;
        }
        else if (n % 100000 < 100000){
            string num = ""+n;
        }
        return num;
    }

};

class Sudoku {
private:
    int ry = 0;
    int cx = 0;
    int iy = 0;
    int jx = 0;
    Board boardObj;
    bool gameOver = false;
    eDerection dir = STOP;
    string number = "0";
    bool solve = false;
public:
    Sudoku(){
        play();
    }
    void play(){
        string ex;
        do {
            while (!gameOver)
            {
                boardObj.displayBoard(ry, cx, iy, jx);
                Input();
                Logic();
                Sleep(100);
            }
            if (solve){
                cout << "Congratulation! You solve it!" << endl;
            }
            else{
                cout << "Oh no. You make some mistakes." << endl;
            }
            cout << "\n1. Restart\n2. Exit in main menu\n3. Save board\n";
            cin >> ex;
            while (ex != "1" && ex != "2" && ex != "3")
            {
                cout << "Error. Try again." << endl;
                cin >> ex;
            }
            if (ex == "3"){
                boardObj.printSVG();
                cout << endl << endl;
            }
        } while (ex != "2" && ex != "3");
    }
    void Logic(){
        switch (dir){
            case LEFT:
                if (jx != 0 || cx != 0){
                    if (jx == 0){
                        jx = 2;
                        cx--;
                    }
                    else {
                        jx--;
                    }

                    dir = STOP;
                }
                break;
            case RIGHT:
                if (jx != 2 || cx != 2){
                    if (jx == 2){
                        jx = 0;
                        cx++;
                    }
                    else {
                        jx++;
                    }

                    dir = STOP;
                }
                break;
            case UP:
                if (iy != 0 || ry != 0){
                    if (iy == 0){
                        iy = 2;
                        ry--;
                    }
                    else {
                        iy--;
                    }

                    dir = STOP;
                }
                break;
            case DOWN:
                if (iy != 2 || ry != 2){
                    if (iy == 2){
                        iy = 0;
                        ry++;
                    }
                    else {
                        iy++;
                    }

                    dir = STOP;
                }
                break;
            default:
                break;
        }
        if (number != "0"){
            boardObj.placeNumber(number, ry, cx, iy, jx);
            number = "0";
        }
    }
    void Input(){
        if (_kbhit())
        {
            switch (_getch()){
                case 'a':{
                    dir = LEFT;
                    break;}
                case 'd':{
                    dir = RIGHT;
                    break;}
                case 'w':{
                    dir = UP;
                    break;}
                case 's':{
                    dir = DOWN;
                    break;}
                case 'x':{
                    gameOver = true;
                    break;}
                case 'c':
                    solve = boardObj.check();
                    gameOver = true;
                    break;
                case '1':{
                    number = "1";
                    break;}
                case '2':{
                    number = "2";
                    break;}
                case '3':{
                    number = "3";
                    break;}
                case '4':{
                    number = "4";
                    break;}
                case '5':{
                    number = "5";
                    break;}
                case '6':{
                    number = "6";
                    break;}
                case '7':{
                    number = "7";
                    cout << number;
                    break;}
                case '8':{
                    number = "8";
                    break;}
                case '9':{
                    number = "9";
                    break;}
            }
        }
    }

};

class Game {
public:
    Game(){ // Start game
        cout << "Welcome" << endl << endl;
        startMenu(); // Show start menu
    }
    int startMenu(){ //Start menu
        string act;
        do {
            cout << "1. Play\n2. Rules\n3. Exit" << endl;
            do {
                cin >> act;
                switch (act[0]) {
                    case '1': { Sudoku sudokuObj; break;} // Play
                    case '2': { rules(); break;} // Rules
                    case '3': { cout << "Goodbye. See you later." << endl; break;} // Exit
                    default: { cout << "Error. Try again." << endl; break;}
                }
            } while (act[0] != '1' && act[0] != '2' && act[0] != '3');
        } while (act[0] != '3');
        return 0;
    }
    void rules(){
        cout << "Rules" << endl << endl;
    }

};

//Main function
int main()
{
	Game gameObj;
	return 0;
}
