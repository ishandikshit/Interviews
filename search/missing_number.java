// Class name must be "Main"
// Libraries included:
// json simple, guava, apache commons lang3, junit, jmock

class Main {
    public static void main(String[] args) {
        
        int n=10;
        int a[] = {1,2,3,4,5,7,8,9,10};
        System.out.println(a);
        int sum = n*(n+1)/2;
        System.out.println (sum);
        int actual_sum=0;
        for(int i=0;i<n-1;i++){
            actual_sum = actual_sum+a[i];
        }
        System.out.println("Missing number is: "+sum-actual_sum);
    }
}
