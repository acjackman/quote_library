class Author < ActiveRecord::Base
  attr_accessible :bio, :birthdate, :birthdateyear, :deathdate, :deathdateyear, :firstname, :lastname, :middlename, :notes, :prefix, :profession, :suffix
  
  validates :lastname, presence: true
end
