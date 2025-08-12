#include<iostream>
#include<cstring>
#include<math.h>
//
int main(){
    std::string inp;
    char*split,*slot;
    double*v,*temp;
    bool mudar;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        v=(double*)calloc(4,sizeof(*v));
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        mudar=false;
        if(v[0]>v[1]){
            v[1]+=v[0];
            v[0]-=v[1];
            v[1]+=v[0];
            v[0]*=-1;
            mudar=true;
        }
        (mudar)?temp=new double(v[1]+v[0]):temp=new double(v[0]);
        for(double i=v[0];i<v[1];i+=v[2]){
            (mudar)?*temp-=v[2]:*temp+=v[2];
            std::cout<<*temp<<"**"<<v[3]<<" = "<<pow(*temp,v[3])<<std::endl;
        }
        std::cout<<std::endl;
        delete temp;
        temp=NULL;
        delete v;
        v=NULL;
    }
}