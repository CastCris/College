#include<iostream>
#include<cstring>
#include<vector>
#include"../bi.cpp"
//
int main(){
    std::vector<std::vector<std::string>>*divisor;
    std::string inp;
    char*split;
    int v[4],*aux,temp,um;
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
            aux=new int(v[0]+v[1]);
            mudar=true;
        }
        divisor=new std::vector<std::vector<std::string>>;
        divisor->resize(2);
        divisor->operator[](0).reserve((v[1]-v[0])/v[3]+1);
        divisor->operator[](1).reserve(v[1]-v[0]);
        for(int i=v[0];i<=v[1];i+=v[2]){
            (mudar)?temp=*aux-i:temp=i;
            (temp%v[3]==0)?um=0:um=1;
            divisor->operator[](um).insert(divisor->operator[](um).end(),std::to_string(temp));
        }
        for(int i=0;i<2;++i){
            std::cout<<"Numero(s)";
            if(i==1){
                std::cout<<" nao";
            }
            std::cout<<" divisiveis por "<<v[3]<<": ";
            for(auto trem:divisor->operator[](i)){
                std::cout<<trem<<" ";
            }
            std::cout<<std::endl;
        }
        delete divisor;
        divisor=NULL;
        if(mudar){
            delete aux;
            aux=NULL;
        }
        (mudar)?mudar=false:mudar;
    }
    std::cout<<conver("Bye, bye!",16)<<std::endl;
    return 0;
}