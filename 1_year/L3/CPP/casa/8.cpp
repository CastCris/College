#include<iostream>
#include<cstring>
#include<vector>
#include"../bi.cpp"
//
int main(){
    std::vector<std::string>*par;
    std::string inp;
    char*split;
    int v[4],temp,*aux;
    bool mudar;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=atoi(split);
            split=std::strtok(NULL," ");
        }
        mudar=false;
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            mudar=true;
            aux=new int(v[0]+v[1]);
        }
        par=new std::vector<std::string>;
        par->reserve((v[1]-v[0])/v[3]+1);
        temp=0;
        do
        {
            temp+=v[2];
            if(mudar){
                if((*aux-temp)%v[3]==0){
                    par->insert(par->end(),std::to_string(*aux-temp));
                }
            } else if(temp%v[3]==0){
                par->insert(par->end(),std::to_string(temp));
            }
        } while(temp<v[1]);
        for(const std::string prin:*par){
            std::cout<<prin<<" ";
        }
        std::cout<<std::endl;
        delete par;
        par=NULL;
        if(mudar){
            delete aux;
            aux=NULL;
        }
    }
    std::cout<<conver("Dooooo",13)<<std::endl;
    return 0;
}