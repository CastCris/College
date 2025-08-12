#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
//
std::string conver(const std::string l,int b){
    std::string out;
    std::map<int,char>*dicionario;
    int e_1=0,e_2,tam,*v;
    char split[l.length()],bibi[l.length()],*letras;
    if(b>10){
        v=(int*)calloc(1,sizeof(*v));
        (b-10>25)?letras=new char[b/25]:letras=new char[1];
        dicionario=new std::map<int,char>[b-9];
        for(int alocar=0;alocar<b-10;++alocar){
            (v[0]+65>90)?v[0]=0:v[0];
            letras[0]=(char)(65+v[0]);
            dicionario->operator[](alocar+10)=*letras;
            ++v[0];
        }
        delete v;
        delete letras;
        v=NULL;
        letras=NULL;
    }
    for(int anali=0;anali<l.length()+1;++anali){
        if((int)l[anali]==32||anali>l.length()-1){
            for(int bgl=0;bgl<e_1;++bgl){
                tam=(int)split[bgl];
                e_2=0;
                while(tam>=1){
                    if(tam%b<10){
                        bibi[e_2]=std::to_string(tam%b)[0];
                    } else{
                        bibi[e_2]=dicionario->operator[](tam%b);
                    }
                    if(tam/(float)b<1){
                        break;
                    }
                    tam/=b;
                    ++e_2;
                }
                for(int cont=0;cont<e_2+1;++cont){
                    out.push_back(bibi[e_2-cont]);
                }
                out.push_back(' ');
            }
            e_1=0;
            
        } else{
            split[e_1]=l[anali];
            ++e_1;
        }
    }
    return out;
}