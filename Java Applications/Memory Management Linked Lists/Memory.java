//Mohammad Abdullah
//260980866


import java.util.LinkedList;


public class Memory {
	//Declaring Memory class fields
	public LinkedList<StringInterval> intervalList;
	public char[] memoryArray;
	public static int idCount;
	
	
	//Creating the InnerClass StringInterval
	public class StringInterval {
		
		public int id;
		public int start;
		public int length;
		
		//Constructing the StringInterval object
		public StringInterval(int id, int start, int length){
			this.id = id;
			this.start = start;
			this.length = length;		
		}
		
	}
	
	//Memory class methods start from here
	
	public Memory(int length) {
		//reseting the static idCount
		idCount = 0;
		//Constructing the required objects
		this.memoryArray = new char[length];
		this.intervalList = new LinkedList<StringInterval>();
		
		
	}
	
	public String get(int id) {
		String tempStr = ""; //Creating a temporary string variable
		
		//Iterates through the linkedlist checking if the id matches
		for (StringInterval tempSI : intervalList) {
			if (tempSI.id == id) {
				
				//Captures the characters through using linked list and the index of the character
				for(int i=tempSI.start; (i<tempSI.start + tempSI.length); i++) {
					tempStr += memoryArray[i]; //Reassigns + Concatenates the string by each character
				}
				return tempStr;
			}
			
		}
		
		return null;
		
	}
	public int get(String s) {
		int tempInt = -1;
		
		//Iterating through the linkedlist
		for (StringInterval tempSI : intervalList) {
			
			//Checks if the String returned from the given id equals the parameter provided
			if(get(tempSI.id).equals(s)) {
				return tempSI.id;
			}
		}
		
		//Returns -1 if String doesn't match
		return tempInt;
	}
	public String remove(int id) {
		String tempStr = "";
		
		//Iterating through the linkedlist
		for (StringInterval tempSI : intervalList) {
			
			//Checks if id exists in the intervallist
			if (tempSI.id == id) {
				tempStr = get(id); //Assigns to tempStr the string that's associated to the id
				
				//Removes the (first occurrence) element from the linkedlist
				intervalList.remove(tempSI);		
				return tempStr; //Returns the String and exits the function
			}
		}
		return null;
	}
	public int remove(String s) {
		int tempInt = -1;
		
		for (StringInterval tempSI : intervalList) {
			
			//Checks if string matches with all the elements present
			//Checks if the string associated to the id of the element equals s
			if (get(tempSI.id).equals(s)) { 
				tempInt = tempSI.id; //Assigns the id to tempInt for returning purposes
				intervalList.remove(tempSI); //Removes the element associated to the string from the list
				
				//Returns id
				return tempInt;
			}
		}
		
		return tempInt;
	}
	//This method counts the number of elements in the array starting from 1
	//equivalent to size of the array
	private int counter() {
		int num = 0;
		for (StringInterval tempSI : intervalList) {
			num+= tempSI.length; //Counts the length for all
		}
		return num;
	}

	public int put(String s) {
		//Some Variables that'll be used
		int mainCount = 0;
		int temp1 = 0;
		int temp2 = 0;
		StringInterval tempSI;
		
		if (memoryArray.length < s.length()) {
			return -1;
		}
		
		//Case EMPTY LIST
		//Checking size of the linkedlist
		if (intervalList.size() == 0) {
			//Tells us list is empty, i.e array is also empty
			mainCount = 0; 
			tempSI = new StringInterval(idCount,mainCount,s.length());
			for (int j=0 ; j<tempSI.length;j++) {
				memoryArray[j+mainCount] = s.charAt(j);
			}
			intervalList.addFirst(tempSI);
			idCount ++;
			return tempSI.id;
			
		}
		//Case 1 Object exists already
		else if (intervalList.size() == 1) {
			//Checking before and after the SI object
			if (s.length() <= intervalList.get(0).start) {
				//object will be made before the existing SI object
				mainCount = 0;
				tempSI = new StringInterval(idCount,mainCount,s.length());
				for (int j=0; j<tempSI.length;j++) {
					memoryArray[j+mainCount] = s.charAt(j);
				}
				intervalList.addFirst(tempSI);
				idCount ++;
				return tempSI.id;
			}
			else if ((memoryArray.length - intervalList.get(0).start - intervalList.get(0).length) >= s.length()) {
				//Object will be made after the existing SI object
				mainCount = intervalList.get(0).start + intervalList.get(0).length;
				tempSI = new StringInterval(idCount,mainCount,s.length());
				for (int j=0; j<tempSI.length;j++) {
					memoryArray[j+mainCount] = s.charAt(j);
				}
				intervalList.addLast(tempSI);
				idCount ++;
				return tempSI.id;
			}
			else if (memoryArray.length - counter() >= s.length()) {
				defragment();
				
				//Copied code from below
				mainCount = counter(); //After rearranging, size of array = new start point
				tempSI = new StringInterval(idCount,mainCount,s.length());
				for (int j=0 ; j<tempSI.length;j++) {
					memoryArray[j+mainCount] = s.charAt(j);
				}
				//Adding to linkedlist at the last location
				intervalList.addLast(tempSI);
				idCount ++;
			
				//Returning the id
				return tempSI.id;
			}
			else {
				return -1;
			}
			
		}
		
		//Case Inserting between elements (2 Objects Exist)
		else if (intervalList.size() > 1){
			
			if ((memoryArray.length - counter()) >= s.length()) { 
				
				//Checking the top of the first element to see if there is space
				if (s.length() <= intervalList.get(0).start) {
					//object will be made before the existing SI object
					mainCount = 0;
					tempSI = new StringInterval(idCount,mainCount,s.length());
					for (int j=0; j<tempSI.length;j++) {
						memoryArray[j+mainCount] = s.charAt(j);
					}
					intervalList.addFirst(tempSI);
					idCount ++;
					return tempSI.id;
				}
				
				for (int i = 0; i < intervalList.size()-1; i++) { //last element is excluded
					
					temp1 = (intervalList.get(i).start +intervalList.get(i).length); //Saving space
					temp2 = (intervalList.get(i+1).start);
					
					if (temp1 != temp2 && (s.length() + temp1) <= temp2) {
						//Above checks if the i'th element's start +length DNE the next element's start
						//TLDR checks if there is enough space between the elements
						
						//If in this if condition, then we have enough space!!
						mainCount = temp1;
						
						//Adding into the array
						tempSI = new StringInterval(idCount,mainCount,s.length());
						for (int j=0; j<tempSI.length; j++) {
							memoryArray[j+mainCount] = s.charAt(j);
						}
						//Adding to LinkedList at the i+1 location
						intervalList.add(i+1, tempSI);
						idCount ++;
						
						//Returning the id
						return tempSI.id;
						
					}
				}
				//If for loop is completed without returning anything
				//Try the last element
				if (memoryArray.length - (intervalList.getLast().start + intervalList.getLast().length)>=s.length()) {
					mainCount = intervalList.getLast().start + intervalList.getLast().length;
					tempSI = new StringInterval(idCount,mainCount,s.length());
					for (int j=0; j<tempSI.length;j++) {
						memoryArray[j+mainCount] = s.charAt(j);
					}
					intervalList.addLast(tempSI);
					idCount ++;
					return tempSI.id;
				}
				//If it still doesn't work, we call defragment
				//Call defragment
				defragment();
			
				//Inserting the SI into the LAST element of the list
			
				mainCount = counter(); //After rearranging, size of array = new start point
				tempSI = new StringInterval(idCount,mainCount,s.length());
				for (int j=0 ; j<tempSI.length;j++) {
					memoryArray[j+mainCount] = s.charAt(j);
				}
				//Adding to linkedlist at the last location
				intervalList.addLast(tempSI);
				idCount ++;
			
				//Returning the id
				return tempSI.id;
				
			}
			else {
				//Cannot add anything (too little space) anything
				return -1;
				
			} 		
		}
		return -1;
	}	
	
	
	public void defragment() {
		
		//Getting rid of gaps in memoryArray & changing the start points of the SI object
		//Some temp variables
		int tempStart = 0;
		int tempCount = 0;
		boolean tempFlag = false;
		
		//Iterating through the memoryArray
		for (int i=0; i<memoryArray.length;i++) {
			tempFlag = false;
			
			//Iterating through the linked list
			for (StringInterval tempSI : intervalList) {
				
				//Checks if memoryArray's index = start of SI object
				if (i == tempSI.start) {
					
					tempStart = tempSI.start;
					//Inserting Stuff
					for (int j=0;j<tempSI.length;j++) {
						memoryArray[(i-tempSI.start+tempCount) +j] = memoryArray[tempSI.start +j];
						//tempCount will count the (total) length of the tempSI objects that were previously inserted
					}
					
					
					//Setting start value of the intervalList to i - tempStart + tempCount
					tempSI.start = i - tempStart +tempCount;
					tempCount = tempSI.length;
					
					//Reassigning i to skip a certain amount of iterations to go to the next space
					i = tempSI.start +tempSI.length-1;
					tempFlag = true;
					break;
				}	
			}
			//Checking if the tempflag is set to true
			if (tempFlag == true) {
				continue;
				//Goes to the next iteration
			}
			
		}
		
	}
	
	public static void main(String[] args) {
		
	}	
	
}