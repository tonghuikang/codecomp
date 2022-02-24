#include "bits/stdc++.h"
using namespace std;
using ll = long long;

struct Project{
	string name;
	int days, score, best_before, roles_cnt;
	vector < pair<int,int> > roles;
	// bool operator<(Project& RHS) const{
	// 	tuple t1 = {-score, days, roles_cnt, best_before};
	// 	tuple t2 = {-RHS.score, RHS.days, RHS.roles_cnt, RHS.best_before};	
	// 	return t1 < t2; 
	// }
};

constexpr int MXN = 100'005;
vector < string > contr_name(MXN);
map < string,int > skill_id, project_id, contr_id;
vector < map < int, int > > skills(MXN); 
vector < int > nxt_free(MXN);
int nxt = 1;
int c, p;

int get_skill_id(string s){
	int & id = skill_id[s];
	if(id == 0)
		id = nxt++;
	return id;
}

vector < Project > projects;


void read_input(char* file_name){
    freopen(file_name, "r", stdin);
    string tmp;

	cin >> c >> p;
	for(int i = 1; i <= c; i++){
		cin >> contr_name[i];
        contr_id[contr_name[i]] = i;
		int n, level;
		cin >> n;
		for(int j = 1; j <= n; j++){
			string skill;
			cin >> skill >> level;
			int id = get_skill_id(skill);
			skills[i][id] = level;
		}
	}
	projects.resize(p);
    int i = 0;
	for(auto & [name, d, s, b, rc, roles] : projects){
		cin >> name >> d >> s >> b >> rc;
        project_id[name] = i++;
		roles.resize(rc);
		for(auto & [ role, level] : roles){
			cin >> tmp >> level;
			role = get_skill_id(tmp);
		}
	}
}



ll read_solution(char* file_name){
    freopen(file_name, "r", stdin);
    int n;
    cin >> n;
    // cout << "N :" << n << endl;
    if(n > p)
        return -1; // invalid
    ll total_score = 0;
    while(n--){
        string p_name, c_name;
        cin >> p_name;
        // cout << "Here project :" << p_name << endl;

        if(project_id.find(p_name) == project_id.end())
            return -1;// invalid project name
        int p_id = project_id[p_name];
        auto pr = projects[p_id];
        int rc = pr.roles_cnt;

        vector < int > p_roles;
        vector < pair<int,int> > needs_mentor, improve;
        int starting_date = 0;
        for(int i = 0; i < rc; i++){
            cin >> c_name;
            int c_id = contr_id[c_name];
            auto & c_skills = skills[c_id];
            auto & [skill, level] = pr.roles[i];
            int & c_level = c_skills[skill];

            if(c_level < level){
                // needs mentor
                needs_mentor.push_back({skill, level});
            }
            if(c_level <= level){
                // will improve
                improve.push_back({c_id, skill});
            }

            // still needs validation if I wasn't fit for the role 
            p_roles.push_back(c_id);
            starting_date = max(starting_date, nxt_free[c_id]);
        }
        //validate mentors 
        for(auto & [skill, level] : needs_mentor){
            bool fnd = 0;
            for(int & mentor : p_roles){
                if(skills[mentor][skill] >= level){
                    fnd = true;
                    break;
                }
            }
            if(!fnd)
                return -1; // invalid
        }
        // improve skills 
        for(auto & [c_id, skill] : improve)
            skills[c_id][skill]++;
//        cout << "Starting :" << starting_date << endl;

        int finish_date = starting_date + pr.days - 1;
        // cout << "Finishing :" << finish_date << endl;
        int delay = max((finish_date + 1) - pr.best_before, 0);
        // cout << "Delay : " << delay << endl;
        for(int i : p_roles){
            nxt_free[i] = finish_date + 1;
        }
        
        // get score 
        int score = max(0, pr.score - delay);
        // cout << "Getting score :" << score << endl;
        total_score += score;
    }
    return total_score;
}





int main(int argc, char ** argv) {
    
    //read_input("e_exceptional_skills.in.txt");
    read_input(argv[1]);
    //int score = read_solution("output-3.txt");
    int score = read_solution(argv[2]);
    cout << score << endl;
}
