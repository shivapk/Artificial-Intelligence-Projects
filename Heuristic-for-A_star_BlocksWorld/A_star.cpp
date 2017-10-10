#include <iostream>       
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>   
#include <map>         
#include <string>
#include <cmath>
#include <ctime>
#include <limits>
using namespace std;
int blocks_count,stacks_count;

class Node
{
public:
    vector< vector<char> > block;
    Node* parent;
    float f,g,h;
    Node()
       {
        f = numeric_limits<float>::infinity();
        g = numeric_limits<float>::infinity();
        h = 0.0;
        parent = NULL;
       }

};

vector<Node*>States;

void problem_generator(Node* current, int temp_bc, int temp_sc) 
{
  vector<vector<char> > current_block; 
  vector <int> single_block;                 

  for (int k=0; k<temp_bc; k++)
     {                                     
      single_block.push_back(k);      
     }

  for (int i=0; i <temp_sc-1; i++) 
    {
      int r = rand() % temp_bc ;  
      vector <char> temp_row;       
      for (int j=0; j<r ; j++)
    {
      int position = rand() % temp_bc;
      temp_row.push_back(single_block[position] + 65);
      swap(single_block[position], single_block[temp_bc-1]);
      temp_bc--;
    }
      current_block.push_back(temp_row);
    }

  if(temp_bc > 0)
    {
      int condition = temp_bc;
      vector <char> temp;
      for (int i=0; i<condition; i++)
        {
          int position = rand() % temp_bc;
          temp.push_back(single_block[position] + 65);
          swap(single_block[position], single_block[temp_bc-1]);
          temp_bc--;
        }
      current_block.push_back(temp);
    }
    
    random_shuffle(current_block.begin(), current_block.end());
  current->block = current_block;
}


void display_state(Node* current){
    vector <vector <char> > temp = current->block;
    for(int i=0; i<temp.size(); i++)
    {
        cout << i+1 << "|-";
        for(int j=0; j<temp[i].size(); j++)
            cout <<temp[i][j];
        cout << endl;
    }
    cout << endl;	
}

Node* display_goal_state(){
            Node* goal = new Node();
            vector<vector<char> > goal_block;
            vector<char> temp_row;
            for(int i=0; i<blocks_count; i++)
            {
                temp_row.push_back(i+65);   //65 for A
            }
            goal_block.push_back(temp_row);
            for(int j=1;j<stacks_count;j++)
            {
            vector<char> empty_row;
            goal_block.push_back(empty_row);
            }
            goal->block = goal_block;
            cout<<"Goal State is: "<<endl;
            display_state(goal);
            return goal;
}

vector<Node*> generateSuccessor(Node* start)
  {
    vector<Node*> row;
    vector<vector<char> > state = start->block;

    int check;
    for (int i=0; i<state.size(); i++)
      {
        if (state[i].size() > 0)
        {
            char tmp = state[i].back();
            state[i].pop_back();
            for (int j=0; j<state.size(); j++)
            {
                check=1;
                if(i!=j)
                {
                state[j].push_back(tmp);
                Node* new_state = new Node();
                new_state->block = state;
                for(int p=0; p<States.size(); p++)
                {
                   if(States[p]->block == state)
                    {
                        row.push_back(States[p]);
                        check=0;
                    }
                }
                if(check==1)
                    row.push_back(new_state);
                state[j].pop_back();
                }
            }
            state[i].push_back(tmp);
        }
      }
    return row;
  }
  
float calculate_heuristic(Node* initial_state, Node* goal)
{  
    vector< vector<char> > now = initial_state->block;
    vector< vector<char> > reqd = goal->block;
    float h;
    float p_2 = 0; 
    int sum_1=0;
    for(int i=1; i<stacks_count; i++)
    {
        p_2 += now[i].size();
        for (int k=0;k<now[i].size();k++){
          for (int l=0;l<k;l++){
            if (now[i][k]>now[i][l]) sum_1+=1;
          }
        }
    }
    float p_0 = 0, p_1 = 0;
    p_0 = p_2;
    int sum_2=0;
    for(int i=0; i<now[0].size(); i++)
    {   
        if(now[0][i] != reqd[0][i])
        {
            p_0++;
            p_1++;
        }
        for (int l=0;l<i;l++){
            if (now[0][i]<now[0][l]) sum_2+=1;
          }
    }
    h =  22.5 * p_0 - 12.5 * p_2 - 1.5*p_1 + 5.5*sum_1 + 10.5*sum_2;
    return h;
}

void Traceback(Node* initial_state, Node* final_state)
{
    vector<Node*> temp;
    temp.push_back(final_state);
    while(final_state->block != initial_state->block)
    {
        temp.push_back(final_state->parent);
        final_state = final_state->parent;
    }
    for(int i=temp.size()-1; i>=0; i--)
    {
        cout << endl;
        cout << "f=" << temp[i]->f <<" g="<<temp[i]->g<<" h="<<temp[i]->h<< endl;
        display_state(temp[i]);
        cout << endl;
    }

    cout << "Depth: " << temp.size()-1 << endl;
    cout << endl;
}

bool isGoal(Node *currState,  Node* goalState)
{
  vector<vector<char> > a = currState->block;
  vector<vector<char> > b = goalState->block;
  if (a.size() != b.size())
    return false;
  for (int p=0; p<a.size(); p++)
    {
      if(a[p].size() != b[p].size())
        return false;
      else
        {
          for (int q=0; q<a[p].size() ; q++)
            if(a[p][q] != b[p][q])
              return false;
        }
    }
  return true;
}

bool isVisited(Node* state)
{
    for(int i=0; i<States.size(); i++)
    {
        if(isGoal(States[i], state))
        {
            return true;
        }
    }
    return false;
}


class node_cmp   
{
public:
    bool operator()(Node* n1, Node* n2)
    {   
        if(n1->f >= n2->f) return true;
        else return false;
    }
};

class Priority_queue_iterate : public priority_queue<Node*, vector<Node*>, node_cmp> {
public:
    const decltype(c.begin()) begin() { return c.begin(); }
    const decltype(c.end()) end() { return c.end(); }
};


int Astar(Node* start, Node* goal) 
{
    int iter = 0; 
    unsigned long frtr_count=0;
    if(start->block == goal->block){
        cout<<"Success. Start state is same as Goal State "<<endl;
        return 0;
    }
    
    Priority_queue_iterate frontier;
    
    start->g = 0.0; 
    start->h = calculate_heuristic(start, goal);
    start->f = start->g + start->h;
    frontier.push(start);
    frtr_count=1;

    while(!frontier.empty())
    {
        frtr_count = max(frtr_count, frontier.size());  
        Node* node = frontier.top();
        frontier.pop();
        
        

        if(isGoal(node, goal))
        {
            cout << "solution path: " << endl;
            Traceback(start, node);
            cout << endl;
            cout << "Final State " << endl; 
            display_state(node); 
            cout << endl;
            cout << "Successly reached Goal State!!!!!!!!!!!!!!!!" << endl;
            cout << "************************See Below for more information***************************" << endl;
            cout << "total_goal_tests= " << iter << endl;
            cout << "max_queue_size= " << frtr_count << endl;
            return 0;
        }
        else
        {    
            if(iter == 10000)
            {
                cout << "Failed to reach the Goal state." << endl;
                cout << "Final State after 10000 goal tests is: " << endl;
                display_state(node);
                return 0;
            }
            iter++;
            vector<Node*> child_node = generateSuccessor(node);
            for(int i = 0; i<child_node.size(); i++)
            {   
                float g_cost= (node->g) + 1;
                if(!isVisited(child_node[i])) 
                {
                     child_node[i]->parent = node;
                     child_node[i]->g= g_cost;
                     child_node[i]->h = calculate_heuristic(child_node[i], goal);
                     child_node[i]->f = child_node[i]->g + child_node[i]->h;
                     States.push_back(child_node[i]);
                     frontier.push(child_node[i]);
                }
                else
                {
                  if((child_node[i]->g) > g_cost)
                        {
                            child_node[i]->parent = node;
                            child_node[i]->g = g_cost; 
                            child_node[i]->f = g_cost + child_node[i]->h;
                                        
                        }
                }             
            }
        }
    }

}

int main()
{           
            cout << "Enter the Number of Blocks space Number of Stacks" << endl;
            cin >> blocks_count >> stacks_count;
            clock_t tStart = clock();
            States.push_back(new Node());
            srand (time(NULL)); 
            problem_generator(States[0],blocks_count,stacks_count);
            cout << "Initial State is: " << endl;
            display_state(States[0]);
            Node* goal=display_goal_state();
            Astar(States[0],goal);
            float a=(float)(clock() - tStart)/CLOCKS_PER_SEC;
            cout<<"Total Time taken: "<<a<<" seconds"<<endl;
            return 0;
}
