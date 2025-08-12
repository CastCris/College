#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
//
int main(){
    std::string inp;
    char*split,*slot;
    double*v;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        split=std::strtok(&inp[0]," ");
        v=new double[2]{0.0,0.0};
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        std::printf("%.2lf^%.2lf = %.2lf\n",v[0],v[1],std::pow(v[0],v[1]));
        delete v;
        v=NULL;
    }
}