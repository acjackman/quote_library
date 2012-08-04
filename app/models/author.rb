class Author < ActiveRecord::Base
  attr_accessible :bio, :birthdate, :birthdateyear, :deathdate, :deathdateyear, :firstname, :lastname, :middlename, :notes, :prefix, :profession, :suffix
  
  validates :lastname, presence: true
  
  def full_name
    name = ""
    name += self.prefix + " " unless self.prefix.blank?
    name += self.firstname + " " unless self.firstname.blank?
    name += self.middlename + " " unless self.middlename.blank?
    name += self.lastname unless self.lastname.blank?
    name += " " + self.suffix unless self.suffix.blank?
    name
  end
end
