#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
//
int main(){
    std::string inp;
    double *v;
    int num;
    for(;;){
        std::getline(std::cin,inp);
        if(inp.length()<1){
            break;
        }
        num=atoi(&inp[0]);
        //1-1474
        v=new double(0);
        *v=(1.0/std::pow((double)5,(double)0.5))*pow(((1+std::pow((double)5,(double)0.5))/2),(double)num)-(1.0/std::pow((double)5,(double)0.5))*pow(((1-std::pow((double)5,(double)0.5))/2),(double)num);
        std::printf("%.0lf\n",*v);

        //2->1476
        /*
        v=new double[3]{0,0,1};
        for(int i=2;i<num+1;++i){
            v[0]=v[1]+v[2];
            v[1]=v[2];
            v[2]=v[0];
        }
        std::printf("%.0lf\n",v[2]);
        */
        delete v;
        v=NULL;
    }
}