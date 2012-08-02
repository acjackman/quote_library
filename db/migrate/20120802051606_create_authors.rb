class CreateAuthors < ActiveRecord::Migration
  def change
    create_table :authors do |t|
      t.string :prefix
      t.string :firstname
      t.string :middlename
      t.string :lastname
      t.string :suffix
      t.date :birthdate
      t.date :deathdate
      t.boolean :birthdateyear, default: true
      t.boolean :deathdateyear, default: true
      t.string :profession
      t.text :bio
      t.text :notes

      t.timestamps
    end
  end
end
