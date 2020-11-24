# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:14:34 2020

@author: RajeshVe
"""
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
stopwords=list(stopwords.words("english"))
extrawords="ipat,test,ticket,tickets,question,show,issue,issues,please,hello,hi,search,tell,find,text,know,explain,information,me,you,keyword,today,tomorrow,yesterday,let,searching,you're,mightn,herself,in,who,that,from,now,some,hers,having,both,only,a,yourselves,she,about,over,did,not,just,ourselves,doesn't,re,too,between,you'd,while,is,each,before,couldn't,then,myself,their,what,i,shan,same,because,hasn,as,isn,me,isn't,and,why,until,which,itself,on,nor,but,by,where,wasn't,was,wasn,being,we,that'll,these,mustn't,be,ve,more,hasn't,couldn,needn,shan't,am,after,so,she's,of,few,needn't,wouldn't,wouldn,there,other,you'll,didn't,haven't,it,once,for,m,this,into,how,yours,off,him,doesn,haven,during,had,no,above,should've,doing,such,again,further,should,most,own,whom,his,out,than,aren,all,hadn,won,they,have,our,if,yourself,he,it's,down,weren,himself,ma,shouldn,you've,does,to,the,at,y,ll,its,those,through,didn,below,or,her,can,themselves,aren't,do,weren't,t,o,are,with,don,an,were,ain,has,hadn't,my,against,here,any,d,ours,you,mightn't,your,been,won't,mustn,them,will,under,very,shouldn't,s,up,don't,when,theirs"
extralist=extrawords.split(",")
stopwords.extend(extralist)

def comparator_q(q1,q2):
    temp_list=[q1,q2]
    for i in range(len(temp_list)):
        query=temp_list[i]
        query=''.join( [letter for letter in query if letter not in string.punctuation]  )#removing punctuations
        query=' '.join( [word for word in query.split() if word not in stopwords] )
        temp_list[i]=query
    vectorizer= TfidfVectorizer()   
    vectorizer=vectorizer.fit_transform(temp_list)
    vectors=vectorizer.toarray() 
    vec1=vectors[0]
    vec2=vectors[1]
    vec1=vec1.reshape(1,-1)#converting 1d vector into 2d vector
    vec2=vec2.reshape(1,-1)
    return(cosine_similarity(vec1,vec2)[0][0])

score=comparator_q('how can i parallel 650v gan mosfets?',
                   'how can i operate 2 gan mosfets 650v in parallel')
print(score)
