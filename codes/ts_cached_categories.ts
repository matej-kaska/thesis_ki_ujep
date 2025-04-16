export const getCachedCategories = async () => {
 const cachedObject = sessionStorage.getItem("categories");
 if (cachedObject) {
  const objects: TSubjectWithCategories[] = JSON.parse(cachedObject);
  if (objects) {
   return objects;
  }
 }
  
 const response = await axios.get("/api/categories/subjects");
 if (response.status === 404) {
  return [blankSubjectWithCategories];
 }
 const loadedObject: TSubjectWithCategories[] =
       response.data.sort((a:Category, b:Category) => a.id - b.id);

 sessionStorage.setItem("categories", JSON.stringify(loadedObject));
 if (loadedObject) {
  return loadedObject;
 }
 return [blankSubjectWithCategories];
};