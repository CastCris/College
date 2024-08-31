#include<iostream>
#include<cstring>
#include"../bi.cpp"
//
int main(){
    std::string inp;
    char*split,*slot;
    double v[3],*aux,bgl,e;
    bool mudar;
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
            aux=new double(v[1]+v[0]);
            mudar=true;
        }
        e=v[0];
        while(e<=v[1]){
            (mudar)?bgl=*aux-e:bgl=e;
            std::cout<<bgl<<" ";
            e+=v[2];
        }
        (mudar)?mudar=false:mudar;
        std::cout<<std::endl;
        delete aux;
        aux=NULL;
        inp.clear();
    }
    std::cout<<conver("Hasta la Vista!",5)<<std::endl;
    return 0;
}