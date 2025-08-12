#include<iostream>
#include<cstring>
#include<cmath>
#include<stdio.h>
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
        v=(double*)calloc(4,sizeof(*v));
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        mudar=false;
        if(v[1]>v[2]){
            v[2]+=v[1];
            v[1]-=v[2];
            v[2]+=v[1];
            v[1]*=-1;
            mudar=true;
        }
        (mudar)?temp=new double(v[1]+v[2]):temp=new double(v[1]);
        (mudar)?v[2]+=v[3]:v[2];
        for(double i=v[1];i<v[2];i+=v[3]){
            (mudar)?*temp-=v[3]:*temp+=v[3];
            printf("%.1lf^%.2lf = %.1lf\n",v[0],*temp,std::pow(v[0],*temp));
            // std::cout<<v[0]<<"^"<<i<<" = "<<std::pow(v[0],i)<<std::endl;
        }
        std::cout<<std::endl;
    }
}