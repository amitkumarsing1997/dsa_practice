
## approach 1 - using map

# def find_union(arr1,arr2):
#     union = []
#     freq = {}

#     for num in arr1:
#         freq[num] = freq.get(num, 0) + 1
    
#     for num in arr2:
#         freq[num] = freq.get(num,0) + 1

#     for num in freq:
#         union.append(num)
#     return union
    

# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]

# union = find_union(arr1, arr2)
# print(union)



# Complexity Analysis
# Time Compleixty : O( (m+n)log(m+n) ) . Inserting a key in map takes logN times, where N is no of elements in map. At max map can store m+n elements {when there are no common elements and elements in arr,arr2 are distntict}. So Inserting m+n th element takes log(m+n) time. Upon approximation across insertion of all elements in worst it would take O((m+n)log(m+n) time.

# Using HashMap also takes the same time, On average insertion in unordered_map takes O(1) time but sorting the union vector takes O((m+n)log(m+n))  time. Because at max union vector can have m+n elements.

# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 

# O(1) {If Space of union ArrayList is not considered}




## approach 2- using set
# def find_union(arr1,arr2):
#     s= set()
#     union = []

#     for num in arr1:
#         s.add(num)

#     for num in arr2:
#         s.add(num)

#     for num in s:
#         union.append(num)
#     return  union

# arr1 = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]

# union = find_union(arr1, arr2)
# print(union)



## approach 3- using two pointers
def find_union(arr1, arr2):
    # pointers
    i, j = 0 ,0 

    #union list
    union = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union)==0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])   
            j += 1  

    while i < len(arr1):    # if any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):     # if any element left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1 
    return union



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)
print(union)



# Time Complexity: O(m+n), Because at max i runs for n times and j runs for m times. When there are no common elements in arr1 and arr2 and all elements in arr1, arr2 are distinct. 

# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 

# O(1) {If Space of union ArrayList is not considered}






      # axios
      #   .post(
      #     APIUrl.baseURL.baseurl + APIUrl.auth.login,
      #     {
      #       email: email.current.value,
      #       password: password.current.value,
      #     },
      #     {
      #       headers: {
      #         "Content-Type": "application/x-www-form-urlencoded",
      #         accept: "application/json",
      #       },
      #     }
      #   )
      #   .then((response) => {
      #     const userDatastatus = response?.data?.success;
      #     const userRefData = response?.data?.body?.content;

      #     const { first_name, last_name, email, mob_no } = userRefData;

      #     console.log(email);
      #     console.log(mob_no);
      #     dispatch(
      #       addUser({
      #         full_name: first_name + " " + last_name,
      #         email: email,
      #         mob_no: mob_no,
      #       })
      #     );

      #     navigate("/browse");

      #     return axios.post(
      #       "http://localhost:8000/auth/main/token",{
      #         username: email,
      #         password: password.current.value,
      #       },
      #       {
      #         headers: {
      #           "Content-Type": "application/x-www-form-urlencoded",
      #           accept: "application/json",
      #         },
      #       }
      #     );
      #   })
      #   .then((tokenResponse) => {
      #     console.log("Token Response", tokenResponse.data);
         

      #     const sendData = async () => {
      #       const url = "http://localhost:8000/user/send/location";
      #       const token = tokenResponse.data.access_token
      #       const data = {
      #         name: first_name,
      #         email: email,
      #         latitude: "19.5",
      #         longitude: "45.5",
      #       };

      #       const headers = {
      #         Authorization: `Bearer ${token}`,
      #         "Content-Type": "application/json",
      #         accept: "application/json",
      #       };

      #       try {
      #         const response = await axios.post(url, data, { headers });
      #         console.log("Response:", response.data);
      #         // Handle response as needed
      #       } catch (error) {
      #         console.log("Erorr occured in third axios-----")
      #         console.error("Error:", error);
      #         // Handle error as needed
      #       }
      #     };

      #     // Call the function to send the data
      #     sendData();
      #   })
      #   .catch((error) => {
      #     console.error("Error:", error);
         
      #     setShowPopup(true);
      #   });
      # }






