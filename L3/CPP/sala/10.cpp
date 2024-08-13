#include<iostream>
#include<cstring>
#include<cstdio>
//
double gaus(double n[3]){
    if(n[0]>n[1]){
        n[1]+=n[0];
        n[0]-=n[1];
        n[1]+=n[0];
        n[0]*=-1;
    }
    n[1]=n[1]-n[2]+1;
    return ((n[0]+n[1])*(int)((n[1]-n[0]+1)/(2+n[2])));
}
int main(){
    std::string inp;
    char*split,*slot;
    double*v,*treco;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        v=new double[3]{0,0,0};
        split=std::strtok(&inp[0]," ");
        for(int i=0;split!=NULL;++i){
            v[i]=strtod(split,&slot);
            split=std::strtok(NULL," ");
        }
        std::printf("%.2lf\n",gaus(v));
    }
}