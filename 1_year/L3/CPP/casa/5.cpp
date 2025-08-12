#include<iostream>
#include<cstring>
#include"../bi.cpp"
//
int main(){
    std::string inp;
    char*split;
    int v[4],*aux,temp;
    bool mudar=false;
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
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            aux=new int(v[1]+v[0]);
            mudar=true;
        }
        std::cout<<"Numeros divisiveis por "<<v[3]<<": ";
        for(int i=v[0];i<=v[1];i+=v[2]){
            (mudar)?temp=*aux-i:temp=i;
            if(temp%v[3]==0){
                std::cout<<temp<<" ";
            }
        }
        if(mudar){
            delete aux;
            aux=NULL;
        }
        (mudar)?mudar=false:mudar;
        std::cout<<std::endl;
    }
    std::cout<<conver("FOR!!!",3)<<std::endl;
    return 0;
}