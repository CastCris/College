#include<iostream>
#include<cstring>
#include"../bi.cpp"
//
int main(){
    std::string inp;
    char*split,*slot;
    double v[3],*temp,*aux;
    bool mudar=false;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            mudar=true;
            aux=new double(v[0]+v[1]);
        }
        temp=new double(v[0]);
        do
        {
            if(!mudar){
                std::cout<<*temp<<" ";
            } else{
                std::cout<<*aux-*temp<<" ";
            }
            *temp+=v[2];
        } while(*temp-v[2]<v[1]-v[2]);
        (mudar)?mudar=false:mudar;
        std::cout<<std::endl;
        delete temp;
        temp=NULL;
        if(mudar){
            delete aux;
            aux=NULL;
        }
    }
    std::cout<<conver("Barigadamm",9);
    return 0;
}