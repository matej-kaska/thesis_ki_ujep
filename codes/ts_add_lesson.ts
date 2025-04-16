const modalAddLessonCallback = async (oldValue: string) => {
 const value = oldValue.trim();
 if (!userData) return console.error("UserData are missing!");
 if (value === "") return openErrorSnackbar("Hodina musí mít název!");
 if (value.length > 63) return openErrorSnackbar("Název nesmí být delší než 63 znaků!");

 const newUserData: iUserData = JSON.parse(JSON.stringify(userData));

 const indexes = getActiveItemsIndexes();
 const lessons = newUserData
  .classes[indexes.activeClassIndex]
  .subjects[indexes. activeSubjectIndex]
  .teaching_units[indexes.activeTeachingUnitIndex]
  .lessons;

 if (lessons.find((item) => (item.name === value)))
  return openErrorSnackbar("Hodina se stejným názvem již existuje!");

 const newLesson: iMenuLesson = {
  _id: uuidv4(),
  name: value,
  published: false,
  days_of_usage: []
 };
 lessons.push(newLesson);

 await Promise.all([
  updateClasses(newUserData.classes),
  updateLesson(newLesson._id, newLesson.name)
 ]);
};