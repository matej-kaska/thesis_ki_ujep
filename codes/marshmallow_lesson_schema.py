class ExtendedItems(Schema):
 name = fields.String(validate=validate.Length(max=1023))
 visibility = fields.String(validate=validate.OneOf(["student", "teacher", "after-lesson"]))
 description = fields.String(validate=validate.Length(max=1023))
 url_to_file = fields.String()

class ActivitySchema(Schema):
 _id = fields.String(validate=validate.Length(equal=36))
 name = fields.String(validate=validate.Length(max=127))
 size = fields.Integer(validate=validate.Range(min=1))
 description = fields.String(validate=validate.Length(max=8191))
 club_url = fields.String()
 icon = fields.String(validate=validate.OneOf(["xxx"]))
 icons = fields.List(fields.String(validate=validate.OneOf(["xxx"])))
 color = fields.String(validate=validate.Length(equal=7))
 files = fields.List(fields.Nested(ExtendedItems))
 urls = fields.List(fields.Nested(ExtendedItems))
 gadgets = fields.List(fields.String(validate=validate.Length(max=255)))

class ActivityList(Schema):
 _id = fields.String(validate=validate.Length(equal=36))
 activities = fields.List(fields.Nested(ActivitySchema))

class Rating(Schema):
 id_of_user = fields.String()
 rating = fields.String(validate=validate.OneOf(["downvote", "upvote", "neutral", "unused"]))

class LessonDatabaseSchema(Schema):
 _id = fields.String(validate=validate.Length(equal=36))
 ts_created = fields.String()
 ts_updated = fields.String()
 name = fields.String(validate=validate.Length(max=68))
 notes = fields.String(validate=validate.Length(max=4095))
 length_in_mins = fields.Integer(validate=validate.Range(min=5, max=720))
 curriculums = fields.List(fields.String)
 goal = fields.String(validate=validate.Length(max=511))
 ratings = fields.List(fields.Nested(Rating))
 activities_list = fields.List(fields.Nested(ActivityList))
 activities_before = fields.List(fields.Nested(ActivitySchema))
 activities_after = fields.List(fields.Nested(ActivitySchema))