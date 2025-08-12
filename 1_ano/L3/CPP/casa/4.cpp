#include<iostream>
#include<cstring>
#include<../bi.cpp>
//
int main(){
    std::string inp;
    char*split,*slot;
    double v[3],*aux,*temp;
    bool mudar;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
        }
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            aux=new double(v[1]+v[0]);
            mudar=true;
        }
        temp=new double(0);
        for(double i=v[0];i<=v[1];i+=v[2]){
            (mudar)?*temp=*aux-i:*temp=i;
            std::cout<<temp<<" ";
        }
        std::cout<<std::endl;
        (mudar)?mudar=false:mudar;
    }
    std::cout<<conver("Enfim for!",7)<<std::endl;
}