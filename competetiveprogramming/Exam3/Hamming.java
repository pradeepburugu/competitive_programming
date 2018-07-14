import java.util.*;

class Hamming{


	public static int function(int x,int y){
		int a[]=new int[8];
		int b[]=new int[8];
		//System.out.println(Arrays.toString(a));
		int count=0;

		int i=7;
		int j=7;
		while(x>0){
			a[i]=x%2;
			x=x/2;
			i--;
		}
		while(y>0){
			b[j]=y%2;
			y=y/2;
			j--;
		}
		for (int k=0;k<=7;k++ ) {
			if(a[k]==b[k]){
				continue;
			}
			else{
				count++;
			}
		}
		return count;


	}
	public static void main(String[] args) {
		System.out.println(function(25,30));
		System.out.println(function(1,4));
		System.out.println(function(25,30));
		System.out.println(function(100,250));
		System.out.println(function(1,30));
		System.out.println(function(0,255));
	}
}