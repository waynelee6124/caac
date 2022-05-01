#include<iostream> 
#include<string> 
#include<cstdlib> 
#include<conio.h> 
#include<ctime> 
#include<windows.h> 
using namespace std; 
void gotoxy(int xpos, int ypos) 
{ 
    COORD scrn; 
    HANDLE hOuput = GetStdHandle(STD_OUTPUT_HANDLE); 
    scrn.X = xpos; scrn.Y = ypos; 
    SetConsoleCursorPosition(hOuput,scrn); 
} 
class Goal{ 
    public: 
        char goal = '*'; 
        int point[2]; 
        void __init__(int P[]){ 
            point[0] = P[0]; 
            point[1] = P[1]; 
        } 
}; 
class Player{ 
    public: 
        char player = 'O'; 
        int point[2]; 
        void __init__(int P[]){ 
            point[0] = P[0]; 
            point[1] = P[1]; 
 
        } 
        void left_move(){            
            point[1] --; 
        } 
        void right_move(){ 
            point[1] ++; 
        } 
        void down_move(){ 
            point[0] ++; 
        } 
        void up_move(){ 
            point[0] --; 
        } 
        bool isOnTheGoal(Goal goal){ 
            for(int i = 0; i < 1000; i++){ 
                if(point[0] == goal.point[0] && point[1] == goal.point[1]){ 
                    return true; 
                } 
            } 
            return false; 
        } 
 
}; 
class Scenes{ 
    private: 
 
 
    public: 
        char frame[30][30]; 
        int wall_points[1000][2]; 
        void __init__(char walls[][30]){ 
            for(int i = 0;i < 1000; i++){ 
                wall_points[i][0] = -1; 
                wall_points[i][1] = -1; 
            } 
 
            for(int i = 0; i < 15; i ++){ 
                for(int j = 0; j < 30; j++){ 
                    frame[i][j] = walls[i][j]; 
                } 
            } 
 
            int k = 0; 
            for(int i = 0; i < 30; i ++){ 
                for(int j = 0; j < 30; j++){ 
                    char c = frame[i][j]; 
 
                    if(c == '+' || c == '-' || c == '|'){ 
                        // cout << i << " " << j << endl; 
                        wall_points[k][0] = i; 
                        wall_points[k][1] = j; 
                        k += 1; 
                    } 
                } 
            } 
 
        } 
        bool isOnTheWall(Player player){ 
            for(int i = 0; i < 1000; i++){ 
                if(wall_points[i][0] == player.point[0] && wall_points[i][1] == player.point[1]){ 
                    return true; 
                } 
            } 
            return false; 
 
        } 
        void batic(Player player, Goal goal){ 
 
            HANDLE hOutput; 
            COORD coord={0,0}; 
            hOutput=GetStdHandle(STD_OUTPUT_HANDLE); 
            char frame2[30][30]; 
            for(int i = 0; i < 30; i ++){ 
                for(int j = 0; j < 30; j++){ 
                    frame2[i][j] = frame[i][j]; 
                } 
            } 
            int x = player.point[0]; 
            int y = player.point[1]; 
            frame2[x][y] = player.player; 
            int x1 = goal.point[0]; 
            int y1 = goal.point[1]; 
            frame2[x1][y1] = goal.goal; 
            //SetConsoleCursorPosition(hOutput, coord); 
            //WriteConsoleOutputCharacterA(*houtpoint, scoreArray, strlen(scoreArray), coord, &bytes); 
            for(int i = 0; i < 15; i++){ 
                //SetConsoleCursorPosition(hOutput, coord); 
                for(int j = 0;j < 30;j ++){ 
                    cout << frame2[i][j]; 
                } 
                cout << endl; 
            } 
 
            //SetConsoleActiveScreenBuffer(*houtpoint); 
        } 
}; 
 
bool game(char maps[][30], int n, int p[], int p1[], int limit_time){ 
    gotoxy(0, 0); 
    srand(time(NULL)); 
    time_t t = time(NULL); 
    time_t second = t; 
 
 
    // game start 
 
    Scenes sc; 
 
    sc.__init__(maps); 
    Player player; 
    player.__init__(p); 
    Goal goal; 
    goal.__init__(p1); 
    sc.batic(player, goal); 
    while(true){ 
        time_t tx = time(NULL); 
  time_t secondx = tx; 
  cout << "#" <<  n << " You have Only" << limit_time - (tx - t) << " sec           " << endl; 
 
        if(_kbhit()){ 
            char cha; 
            cha = getch(); 
            if(cha == 'a'){ 
                player.left_move(); 
                //sc.batic(player, goal); 
            } 
            else if(cha == 'd'){ 
                player.right_move(); 
                //sc.batic(player, goal); 
            } 
            else if(cha == 'w'){ 
                player.up_move(); 
                //sc.batic(player, goal); 
            } 
            else if(cha == 's'){ 
                player.down_move(); 
                //sc.batic(player, goal); 
            } 
            else if(cha == 'q'){ 
                break; 
            } 
            else if(cha == 'f'){ 
                sc.batic(player, goal); 
            } 
            if(player.isOnTheGoal(goal)){ 
                system("CLS"); 
                cout << "you win" << endl; 
                return true; 
            } 
            if(sc.isOnTheWall(player)){ 
 
                return game(maps, n, p, p1, limit_time - (tx - t)); 
            } 
        } 
        if(limit_time - (tx - t) <= 0){ 
            system("CLS"); 
            cout << "you lose" << endl; 
            return false; 
        } 
            //sc.batic(player, goal); 
 
 
        sc.batic(player, goal); 
 
        gotoxy(0, 0); 
 
    } 
} 
void __init__(){ 
    HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE); 
    CONSOLE_CURSOR_INFO CursorInfo; 
    GetConsoleCursorInfo(handle, &CursorInfo);//获取控制台光标信息 
    CursorInfo.bVisible = false; //隐藏控制台光标 
    SetConsoleCursorInfo(handle, &CursorInfo);//设置控制台光标状态 
    system("mode con cols=60 lines=17");//改变宽高 
} 
int main(void){ 
    __init__(); 
    bool iswin  = true; 
    cout << "press s to start" << endl; 
    while(true){ 
        if(_kbhit){ 
            char cha; 
            cha = getch(); 
            if(cha == 's'){ 
                break; 
            } 
        } 
    } 
    if (iswin){ 
        cout << "please wait" << endl; 
        char maps[30][30] = { 
            "+---------------------+", 
            "|                     |", 
            "|-------+---+---+---+ |", 
            "|   |   |   |   |   | |", 
            "| |   | | |   |   |   |", 
            "+-+---+ + +---+-+-+---+", 
            "|       |       |     |", 
            "| ------+------   +-- |", 
            "|               | |   |", 
            "+---------------+-+---+", 
        }; 
        //cout << "第一關" << endl; 
        int p[2] = {1, 1}; 
        int p1[2]= {4, 1}; 
        Sleep(2000); 
        iswin = game(maps, 1, p, p1, 40); 
    } 
    // ----------------------------------- 
    if(iswin){ 
        char maps2[30][30] = { 
            "+-+---+-+-------+-----+", 
            "| |   | |   |   |     |", 
            "| | |     |   | +---+ |", 
            "|   +---+ +---+-+     |", 
            "+---+              ++ |", 
            "+---+------+----+--++ |", 
            "|          |   ++     |", 
            "+------+ + | +    +++ |", 
            "|        |   | ++ +++ |", 
            "+--------+---+-++-+-+-+", 
        }; 
        int p2[2] = {1, 1}; 
        int p3[2] = {8, 1}; 
        Sleep(2000); 
        gotoxy(0, 0); 
        iswin = game(maps2, 2, p2, p3, 30); 
    } 
    if(iswin){ 
        char maps3[30][30]={ 
            "+-----------------+", 
            "|    |      |     |", 
            "| +- +------+- -+ |", 
            "| ++-+ |    |  |  |", 
            "|         +     | |", 
            "|---+ +--+- ---+--|", 
            "|   | |  +        |", 
            "|---+-+--------- -+", 
            "|                 |", 
            "|-----------------+", 
        }; 
        int p4[2] = {8, 1}; 
        int p5[2] = {2, 4}; 
        Sleep(2000); 
        gotoxy(0, 0); 
        iswin = game(maps3, 3, p4, p5, 30); 
    } 
 
    cout << "press q to quit" << endl; 
    while(true){ 
        if(_kbhit){ 
            char cha; 
            cha = getch(); 
            if(cha == 'q'){ 
                break; 
            } 
        } 
    } 
} 
